import pdfplumber

# PDFExtractor Class
class PDFExtractor:
    def __init__(self, pdf_path: str):
        self.pdf_path = pdf_path

    def extract_text(self) -> str:
        guidelines_text = ""
        with pdfplumber.open(self.pdf_path) as pdf:
            for page in pdf.pages:
                guidelines_text += page.extract_text()
        return guidelines_text