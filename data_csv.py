import csv

def write_info(info):
    with open("data.csv", "a", encoding="utf-8") as file:
        file.write(info)
    return "Заметка добавлена"




def number_lines():
    with open("data.csv", "r",encoding="utf-8") as file:
        lst = file.readlines()
        return lst



def search_note_info(arg):
    with open("data.csv", "r",encoding="utf-8") as file:
        lst = file.readlines()
        note_accepted = []
        for line in lst:
            if arg in line.lower():
                note_accepted.append(line)
        return lst, note_accepted, "Поиск завершен"


def change_or_delete_note(old_note, delete_note, new_line=None):
    with open("data.csv", "w", encoding="utf-8") as file:
        for line in old_note:
            if line == delete_note:
                if new_line:
                    file.write(new_line)
                continue
            file.write(line)
    return "заметка удалена" if not new_line else "заметка изменена"

def view_all():
    with open("data.csv", "r",encoding="utf-8") as file:
        return file.read()



