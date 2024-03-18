from viewer import*
from data_csv import*

def main():
    while True:
        ans = select()
        if ans == 1:
            note_name = get_note_info()
            result_note = write_info(note_name)
            print_info(result_note)
        if ans == 2:
            option = get_search_option()
            all_notes, note_accepted, result_note = search_note_info(option)
            print_info(note_accepted, result_note)
        if ans == 3:
            option = get_search_option()
            all_notes, note_accepted, result_note = search_note_info(option)
            print_info(note_accepted, result_note)
            selected_note_numb_of_str=select_str_in_note()
            result_note=change_or_delete_note(all_notes, note_accepted[selected_note_numb_of_str])
            print_info(result_note)
        if ans == 4:
            option = get_search_option()
            all_notes, note_accepted, result_note = search_note_info(option)
            print_info(note_accepted, result_note)
            selected_note_numb_of_str=select_str_in_note_edit()
            new_line = get_note_info()
            result_note = change_or_delete_note(all_notes, note_accepted[selected_note_numb_of_str], new_line)
            print_info(result_note)
        if ans == 5:
            result_note = view_all()
            print_info(result_note)
        if ans == 6:
            break

main()