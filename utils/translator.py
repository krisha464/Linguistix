from deep_translator import GoogleTranslator

SUPPORTED_LANGS = {
    "auto": "Auto-detect",
    "en": "English",
    "es": "Spanish",
    "fr": "French",
    "de": "German",
    "it": "Italian",
    "ja": "Japanese",
    "ko": "Korean",
    "zh-CN": "Chinese (Simplified)",
    "hi": "Hindi",
    "bn": "Bengali",
    "te": "Telugu",
    "mr": "Marathi",
    "ta": "Tamil",
    "gu": "Gujarati",
    "kn": "Kannada",
    "ml": "Malayalam",
    "pa": "Punjabi",
    "ar": "Arabic",
    "ru": "Russian",
    "pt": "Portuguese"
}

def detect_and_translate(text, target_lang="en", source_lang="auto"):
    """
    Translation function with auto-detection awareness.
    """
    try:
        if not text.strip():
            return "", "unknown"
        
        translator = GoogleTranslator(source=source_lang, target=target_lang)
        translated = translator.translate(text)
        
        # If source was auto, we don't know the exact lang without extra call
        # but for a 'simpel' app, returning the translation is the priority.
        return translated, source_lang
    except Exception as e:
        return f"Error: {str(e)}", "unknown"
