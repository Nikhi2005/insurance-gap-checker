import fitz
import os
import pytesseract

from pdf2image import convert_from_path

pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)

input_folder = "data/raw_docs"
output_folder = "data/extracted_text"

os.makedirs(output_folder, exist_ok=True)


def extract_with_pymupdf(pdf_path):

    doc = fitz.open(pdf_path)

    text = ""

    for page in doc:
        text += page.get_text()

    doc.close()

    return text.strip()


def extract_with_ocr(pdf_path):

    images = convert_from_path(pdf_path)

    text = ""

    for image in images:
        text += pytesseract.image_to_string(image)

    return text.strip()


for filename in os.listdir(input_folder):

    if filename.endswith(".pdf"):

        pdf_path = os.path.join(input_folder, filename)

        txt_filename = filename.replace(".pdf", ".txt")

        output_path = os.path.join(output_folder, txt_filename)

        text = extract_with_pymupdf(pdf_path)

        if not text:

            print(f"OCR Used -> {filename}")

            text = extract_with_ocr(pdf_path)

        else:

            print(f"PyMuPDF Used -> {filename}")

        with open(output_path, "w", encoding="utf-8") as file:
            file.write(text)

print("\nAll documents processed successfully.")