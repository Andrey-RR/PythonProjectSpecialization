import datetime
from data_csv import number_lines
def select():
    get_select = int(input("Выберите действие: \n1-создание заметки  \n2-поиск заметки \n3-удаление заметки \n4-редактирование заметки \n5-показать все заметки \n6-выход"))
    return get_select

def get_note_info():
    time = datetime.datetime.now()
    note_id = number_lines()
    note_id_row = str(len(note_id)+1)
    note_title = input("Введите заголовок заметки: ")
    text_note = input("Введите текст заметки: ")
    res_info = note_id_row + ") " + time.strftime('%d-%m-%Y  %H %M') + "; " + note_title + "; " + text_note +"\n"
    return res_info


def print_info(*args):
    for res in args:
        if isinstance(res, list):
            counter = 1
            for string in res:
                print(f'{counter}) {string.strip()}')
                counter += 1
        if isinstance(res,str):
            print(res)


def get_search_option():
    search_info = input("Введите ключевое слово для поиска или дату заметки в формате ДД-ММ-ГГГГ: ").lower()
    return search_info

def select_str_in_note():
    num = int(input("Выберите строку для удаления: "))
    return num - 1

def select_str_in_note_edit():
    num = int(input("Выберите строку для редактирования: "))
    return num - 1