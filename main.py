from converters.image_to_text import image_to_text
from converters.pdf_to_text import pdf_to_text
from converters.docx_to_text import docx_to_text
from converters.txt_to_text import txt_to_text
from converters.xlsx_to_text import xlsx_to_text
from converters.odt_to_text import odt_to_text
import os
import g4f
import logging

#file_path = r'test_files\test.txt'
#theme = 'Япония 21 века'

#словарь со всеми функциями конвертерами
converters = {
    '.jpeg': image_to_text,
    '.png': image_to_text,
    '.pdf': pdf_to_text,
    '.docx': docx_to_text,
    '.txt': txt_to_text,
    '.xlsx': xlsx_to_text,
    '.odt': odt_to_text
}

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

handler = logging.FileHandler(f"{__name__}.log", mode='a')
formatter = logging.Formatter("%(name)s %(asctime)s %(levelname)s %(message)s")

handler.setFormatter(formatter)
logger.addHandler(handler)

def ask_bot(text: str) -> None:
    '''
    takes text
    return None
    '''

    response = g4f.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[{'role': 'user', 'content': text}],
    )

    if response:
        logger.info(f'ChatGPT response: {response}')
    else:
        logger.error(f'No response from ChatGPT')

def get_text(file_path: str) -> None:
    '''
    takes file_path
    return None
    '''
    try:
        _, file_extension = os.path.splitext(file_path)
    except:
        logger.error(f'Incorrect file path')

    if file_extension in converters:
        return converters[file_extension](file_path)
    else:
        logger.error(f'Unsupported file extension')

def get_request(theme, file_path) -> str:
    '''
    takes None
    return: str
    '''

    result = get_text(file_path)
    text = ' '.join(result)
    message = f'Соответствует ли данный текст: "{text}" теме: "{theme}"'

    return message

#вызов главной функции
if __name__ == '__main__':
    theme = input('Type your theme to work with: ')
    file_path = input('Please copy the file path: ')
    file_path.encode('unicode_escape')

    message = get_request(theme, file_path)

    ask_bot(message)
