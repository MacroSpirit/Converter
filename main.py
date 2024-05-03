from converters.image_to_text import image_to_text
from converters.pdf_to_text import pdf_to_text
from converters.docx_to_text import docx_to_text
from converters.txt_to_text import txt_to_text
from converters.xlsx_to_text import xlsx_to_text
from converters.odt_to_text import odt_to_text
import os
import g4f

file_path = r'test_files\test.txt'
theme = 'Япония 21 века'

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

def ask_bot(text: str) -> None:
    '''
    takes text
    return None
    '''

    response = g4f.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[{'role': 'user', 'content': text}],
    )

    print(response)

def get_text(file_path: str) -> None:
    '''
    takes file_path
    return None
    '''

    _, file_extension = os.path.splitext(file_path)

    if file_extension in converters:
        return converters[file_extension](file_path)
    else:
        print('Unsupported file extension')

def get_request() -> str:
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
    message = get_request()

    ask_bot(message)
