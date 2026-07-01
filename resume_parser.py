import pdfplumber
from docx import Document
import tempfile
import os


def extract_text(uploaded_file):

    if uploaded_file is None:
        return ""

    suffix = uploaded_file.name.split(".")[-1]

    with tempfile.NamedTemporaryFile(delete=False, suffix="."+suffix) as tmp:
        tmp.write(uploaded_file.read())
        temp_path = tmp.name

    text = ""

    try:

        if suffix.lower() == "pdf":

            with pdfplumber.open(temp_path) as pdf:

                for page in pdf.pages:

                    page_text = page.extract_text()

                    if page_text:
                        text += page_text + "\n"

        elif suffix.lower() == "docx":

            doc = Document(temp_path)

            for para in doc.paragraphs:

                text += para.text + "\n"

    finally:

        os.remove(temp_path)

    return text.lower()