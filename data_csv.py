import csv

def write_info(info):
    with open("data.csv", "a", encoding="utf-8") as file:
        file.write(info)
    return "Заметка добавлена"




def number_lines():
    with open("data.csv", "r",encoding="utf-8") as file:
        lst = file.readlines()
        return lst

