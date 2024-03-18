from viewer import*
from data_csv import*

def main():
    while True:
        ans = select()
        if ans == 1:
            note_name = get_note_info()
            result_note = write_info(note_name)
            print_info(result_note)


main()