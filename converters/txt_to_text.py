
def txt_to_text(file_path:str) -> list:
    '''
    takes file_path
    return list of strings
    '''

    with open(file_path, encoding='utf-8') as file:
        text = [line.strip() for line in file.readlines() if line.strip()]

        return text
