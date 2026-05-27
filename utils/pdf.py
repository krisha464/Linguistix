from fpdf import FPDF

def create_pdf(text, title="Translation"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(40, 10, title)
    pdf.ln(20)
    pdf.set_font("Arial", size=12)
    # Handle non-latin1 characters by replacing them to avoid encoding errors
    safe_text = text.encode('latin-1', 'replace').decode('latin-1')
    pdf.multi_cell(0, 10, safe_text)
    
    # Get the PDF content
    pdf_out = pdf.output(dest='S')
    
    # If it's already bytes or bytearray, return as bytes
    if isinstance(pdf_out, (bytes, bytearray)):
        return bytes(pdf_out)
    # If it's a string, encode it
    return pdf_out.encode('latin-1')
