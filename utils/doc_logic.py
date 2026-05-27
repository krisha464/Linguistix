import fitz  # PyMuPDF
from docx import Document
import io

def extract_text_from_doc(file_bytes, file_type):
    """
    Extracts text from PDF or DOCX files.
    """
    text = ""
    try:
        if file_type == "application/pdf":
            # Extract from PDF
            doc = fitz.open(stream=file_bytes, filetype="pdf")
            for page in doc:
                text += page.get_text()
            doc.close()
            
        elif "officedocument.wordprocessingml.document" in file_type:
            # Extract from DOCX
            doc = Document(io.BytesIO(file_bytes))
            for para in doc.paragraphs:
                text += para.text + "\n"
        
        elif file_type == "text/plain":
            # Extract from TXT
            text = file_bytes.decode("utf-8", "ignore")
            
        return text.strip()
    except Exception as e:
        return f"ERROR: Failed to parse document: {str(e)}"
