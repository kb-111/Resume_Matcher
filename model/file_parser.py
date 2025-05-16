import docx2txt
import PyPDF2

def extract_text_from_file(file):
    if file.name.endswith(".pdf"):
        reader = PyPDF2.PdfReader(file)
        return " ".join([page.extract_text() for page in reader.pages])
    elif file.name.endswith(".docx"):
        return docx2txt.process(file)
    return ""
