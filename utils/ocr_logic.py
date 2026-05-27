from PIL import Image, ImageDraw, ImageFont
import numpy as np

# Initialize the reader only once - globally
_READER = None
_INIT_ERROR = None

def extract_text_from_image(image_path_or_bytes):
    """
    Extracts text from an image using EasyOCR.
    Handles Lazy Loading and Torch DLL errors on Windows.
    """
    global _READER, _INIT_ERROR
    
    # If we already had a critical error (like DLL failed), don't keep trying
    if _INIT_ERROR:
        return f"ERROR: {_INIT_ERROR}"

    try:
        import easyocr
        
        if _READER is None:
            # English as primary for OCR
            _READER = easyocr.Reader(['en'], gpu=False) # Force CPU to avoid CUDA DLL issues
        
        # Open image
        img = Image.open(image_path_or_bytes)
        img_np = np.array(img)
        
        # Read text
        results = _READER.readtext(img_np)
        
        # Combine text parts
        extracted_text = " ".join([res[1] for res in results])
        return extracted_text if extracted_text.strip() else "No readable text found."
    except ImportError as e:
        _INIT_ERROR = "Torch/EasyOCR dependencies missing. Try: pip install torch easyocr"
        return f"ERROR: {_INIT_ERROR}"
    except Exception as e:
        err_msg = str(e)
        if "DLL load failed" in err_msg or "torch" in err_msg.lower():
            _INIT_ERROR = """
            Windows is missing C++ Redistributables required for OCR.
            Please download and install it from the official Microsoft link:
            [Download Visual C++ Redistributable](https://aka.ms/vs/17/release/vc_redist.x64.exe)
            (After installing, you may need to restart the app).
            """
        else:
            _INIT_ERROR = f"OCR failed to initialize: {err_msg}"
        return f"ERROR: {_INIT_ERROR}"

def translate_image_content(image_path_or_bytes, target_lang, translator_func):
    """
    Performs 'visual translation' by replacing original text in the image with translated text.
    Correctly aggregates text for faster translation and better visual coherence.
    """
    global _READER
    try:
        import easyocr
        if _READER is None:
             _READER = easyocr.Reader(['en'], gpu=False)
        
        # 1. Load Image and prepare resources
        img = Image.open(image_path_or_bytes).convert("RGB")
        draw = ImageDraw.Draw(img)
        img_np = np.array(img)
        
        # 2. Extract Text with Coordinates
        # (Detail=1 to get bounding boxes)
        results = _READER.readtext(img_np, detail=1)
        if not results:
            return None, "No text found to translate."

        results = [res for res in results if res[1].strip()]
        if not results:
            return None, "All text found was too small or unreadable."

        # 3. Batch Translation for Performance
        separator = " ||| "
        combined_text = separator.join([res[1] for res in results])
        
        translated_all, _ = translator_func(combined_text, target_lang, "auto")
        translated_parts = translated_all.split(separator)
        
        if len(translated_parts) < len(results):
            translated_parts += [""] * (len(results) - len(translated_parts))

        # 4. Draw Translated Text
        for i, (bbox, original_text, conf) in enumerate(results):
            translated_text = translated_parts[i].strip()
            if not translated_text: continue
            
            # Use tighter bounding box logic
            xs = [p[0] for p in bbox]
            ys = [p[1] for p in bbox]
            tl_x, tl_y = int(min(xs)), int(min(ys))
            br_x, br_y = int(max(xs)), int(max(ys))
            
            box_w = br_x - tl_x
            box_h = br_y - tl_y
            if box_w <= 3 or box_h <= 3: continue

            # --- SMART MASKING ---
            try:
                # Sample background color near the top-left to avoid text pixels
                patch = img.crop((tl_x, tl_y, min(tl_x+5, br_x), min(tl_y+5, br_y)))
                patch_np = np.array(patch)
                bg_color = tuple(np.median(patch_np, axis=(0, 1)).astype(int))
            except:
                bg_color = (255, 255, 255)

            # Determine text color based on luminance
            luma = (0.299 * bg_color[0] + 0.587 * bg_color[1] + 0.114 * bg_color[2]) / 255
            text_color = (0,0,0) if luma > 0.55 else (245,245,245)

            # Fill original area with sampled background
            draw.rectangle([tl_x, tl_y, br_x, br_y], fill=bg_color)
            
            # --- FONT RENDERING ---
            # Increase starting size for better detail, then shrink to fit
            font_size = int(box_h * 0.75) 
            try:
                # Try many common font paths to ensure we don't hit load_default()
                fonts_to_try = [
                    "C:\\Windows\\Fonts\\arial.ttf", 
                    "arial.ttf", 
                    "DejaVuSans.ttf", 
                    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
                ]
                font = None
                for fp in fonts_to_try:
                    try:
                        font = ImageFont.truetype(fp, font_size)
                        break
                    except: continue
                if not font: font = ImageFont.load_default()
            except:
                font = ImageFont.load_default()
            
            # Refined centering and fit
            try:
                # Check text width vs box width
                t_bbox = draw.textbbox((0, 0), translated_text, font=font)
                t_w, t_h = t_bbox[2]-t_bbox[0], t_bbox[3]-t_bbox[1]
                
                # Shrink if too wide
                if t_w > box_w * 0.95:
                    font_size = int(font_size * (box_w * 0.9 / t_w))
                    font_size = max(font_size, 8)
                    font = ImageFont.truetype(fonts_to_try[0], font_size) if font else ImageFont.load_default()
                    t_bbox = draw.textbbox((0, 0), translated_text, font=font)
                    t_w, t_h = t_bbox[2]-t_bbox[0], t_bbox[3]-t_bbox[1]

                pos_x = tl_x + (box_w - t_w) // 2
                pos_y = tl_y + (box_h - t_h) // 2
                draw.text((pos_x, pos_y), translated_text, fill=text_color, font=font)
            except:
                draw.text((tl_x + 2, tl_y + (box_h//4)), translated_text, fill=text_color, font=font)
        
        return img, None
    except Exception as e:
        import traceback
        return None, f"{str(e)}\n{traceback.format_exc()}"
