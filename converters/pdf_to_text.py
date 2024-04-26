from pdf2image import convert_from_path
import os
from pytesseract import pytesseract
from PIL import Image
from converters.image_to_text import image_to_text


path_to_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
pytesseract.tesseract_cmd = path_to_tesseract
poppler_path = r'C:\Users\Клим\Downloads\Release-24.02.0-0\poppler-24.02.0\Library\bin'

def pdf_to_text(file_path) -> list:
    images = convert_from_path(file_path, poppler_path=poppler_path)
    text = []

    for image in images:
        image.save('image.jpeg', 'JPEG')
        result = image_to_text('image.jpeg')
        text.extend(result)
        os.remove('image.jpeg')

    return text
