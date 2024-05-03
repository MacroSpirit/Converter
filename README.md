Приложение конвертирует файлы с различными расширениями в питоновский объект (список) и проверяет, совпадает ли текст указанной теме.

Для запуска необходимо:

Затем устанавливаем Tesseract и копируем путь до exe файла в файл constants.py, и заменяем константу PATH_TO_TESSERACT. Сcылка на Tesseract - https://github.com/UB-Mannheim/tesseract/wiki

Также нужно скачать Poppler и скопировать путь до содержимого папки bin в константу POPPLER_PATH. Ccылка на Poppler - https://github.com/oschwartz10612/poppler-windows/releases/

Установить зависимости из файла requirements.txt pip install -r requirements.txt

Указать путь до файла, который вы хотите конверировать в текст, в переменной file_pathв файле main.py 

Указать заданную тему в переменной theme в файле main.py

Запустить файл main.py
