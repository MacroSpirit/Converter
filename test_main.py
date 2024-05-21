from converters.image_to_text import image_to_text
from converters.pdf_to_text import pdf_to_text
from converters.docx_to_text import docx_to_text
from converters.txt_to_text import txt_to_text
from converters.xlsx_to_text import xlsx_to_text
from converters.odt_to_text import odt_to_text


def string_check(result):
    flag = True

    for item in result:
        if not isinstance(item, str):
            flag = False

    return flag

def test_pdf():
    result = pdf_to_text(r'test_files\test.pdf')
    assert isinstance(result, list)
    assert result != None
    assert string_check(result) == True


def test_docx():
    result = docx_to_text(r'test_files\test.docx')
    assert isinstance(result, list)
    assert result != None
    assert string_check(result) == True


def test_odt():
    result = odt_to_text(r'test_files\test.odt')
    assert isinstance(result, list)
    assert result != None
    assert string_check(result) == True


def test_image():
    result = image_to_text(r'test_files\test.png')
    assert isinstance(result, list)
    assert result != None
    assert string_check(result) == True


def test_txt():
    result = txt_to_text(r'test_files\test.txt')
    assert isinstance(result, list)
    assert result != None
    assert string_check(result) == True


def test_xlxs():
    result = xlsx_to_text(r'test_files\test.xlsx')
    assert isinstance(result, list)
    assert result != None
    assert string_check(result) == True
