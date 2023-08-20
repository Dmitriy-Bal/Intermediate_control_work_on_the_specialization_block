from interface import Interface
from notes import Notes

#Управление приложением

def start():
    notes = Notes()
    interface = Interface()
    while True:
        match interface.main_menu():
            case "1":
                title = interface.title()
                if not notes.check_exists_note(title=title):
                    notes.create_note(title,interface.text())
                else:
                    interface.error_exists_note()
                    interface.press_enter()
            case "2":
                notes.save_in_file(file_name = interface.file_name())
            case "3":
                notes.read_in_file(file_name=interface.file_name(),read_parametr=interface.read_menu())
            case "4":
                interface.clear()
                if interface.watch_notes_menu():
                    parametr = interface.parametrs_menu()
                    if parametr == "1":
                        notes.parametrs_list_notes(parametr_id = parametr, parametr=interface.data(),show_data_parametr=interface.date_menu())
                    elif parametr == "2":
                        notes.parametrs_list_notes(parametr_id=parametr, parametr=interface.title(),show_data_parametr=interface.date_menu())
                    else:
                        notes.parametrs_list_notes(parametr_id=parametr, parametr=interface.text(),show_data_parametr=interface.date_menu())
                    interface.press_enter()
                else:
                    notes.list_notes(list_parametr=interface.date_menu())
                    interface.press_enter()
            case "5":
                if not notes.edit_note(interface.title(),interface.text()):
                    interface.title_not_found()
                else:
                    interface.seccess()
                    interface.press_enter()
            case "6":
                parametr = interface.parametrs_menu()
                if parametr == "1":
                    notes_dict = notes.parametrs_list_notes(parametr_id=parametr, parametr=interface.data(),show_data_parametr=interface.date_menu())
                elif parametr == "2":
                    notes_dict = notes.parametrs_list_notes(parametr_id=parametr, parametr=interface.title(),show_data_parametr=interface.date_menu())
                else:
                    notes_dict = notes.parametrs_list_notes(parametr_id=parametr, parametr=interface.text(),show_data_parametr=interface.date_menu())
                if notes_dict:
                    while (id_note := interface.choose_note()) not in notes_dict:
                        print("Не правильный ввод данных! Повторите ввод данных!")

                    notes.remove_note(id_note=id_note,notes_dict=notes_dict)
                    interface.successfully_remove()
                    interface.press_enter()
                else:
                    interface.error_find_note()
                    interface.press_enter()
            case "7":
                exit(1)
            case _:
                interface.repeat_input()
                interface.press_enter()