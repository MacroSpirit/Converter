from PIL import Image
from pytesseract import pytesseract
from constants import PATH_TO_TESSERACT


pytesseract.tesseract_cmd = PATH_TO_TESSERACT

def image_to_text(file_path: str) -> list:
    '''
    takes file_path
    return list of strings
    '''

    img = Image.open(file_path)
    data = pytesseract.image_to_string(img, lang='rus')
    text = data.split('\n')
    for element in text:
        if not element:
            text.remove(element)

    return text

