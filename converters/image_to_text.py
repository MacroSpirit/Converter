from PIL import Image
from pytesseract import pytesseract


path_to_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
pytesseract.tesseract_cmd = path_to_tesseract

def image_to_text(file_path) -> list:
    img = Image.open(file_path)
    data = pytesseract.image_to_string(img, lang='rus')
    text = data.split('\n')
    for element in text:
        if not element:
            text.remove(element)

    return text

