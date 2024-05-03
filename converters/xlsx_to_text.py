import openpyxl


def xlsx_to_text(file_path: str) -> list:
    '''
    takes file_path
    return list of strings
    '''

    book = openpyxl.open(file_path, read_only=True)
    sheet = book.active
    text = []

    for row in sheet.iter_rows():
        for cell in row:
            if cell.value:
                text.append(cell.value)

    return text
