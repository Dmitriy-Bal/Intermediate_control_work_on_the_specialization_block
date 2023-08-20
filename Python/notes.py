from datetime import datetime
import json
from note import Note
import os


# Класс создания листа с заметками
class Notes:
    # Конструктор класса
    def __init__(self):
        self.notes_list = []

    # Функция создания заметки
    def create_note(self,title, text,data = None):
        # Добавление заметки в список
        self.notes_list.append(Note(title=title,text=text,data=data if data else datetime.now()))

    # Функция отчистки списка заметок
    def clear_notes(self):
        self.notes_list = []

    # Функция проверки существования заметки
    def check_exists_note(self,title):
        for note in self.notes_list:
            if note.get_title() == title:
                return True
        return False

    # Функция сохранения заметок в файл
    def save_in_file(self,file_name):
        # Используйте формат JSON для сохранения заметок
        out = []
        if not os.path.exists(file_name):
            open(file_name, 'a').close()
        with open(f'{file_name}.json', 'w') as f:
            for note in self.notes_list:
                out.append(note.get_all())
            json.dump(out, f)

    # Функция чтения заметок из файла
    def read_in_file(self, file_name, read_parametr):
        with open(f'{file_name}.json') as json_file:
            data = json.load(json_file)
            if not read_parametr:
                self.clear_notes()
            for note in data:
                self.create_note(text=note[0], title=note[1], data=datetime.fromisoformat(note[2]))

    # Функция чтения списка заметок
    def list_notes(self,list_parametr):
        # Пройдите циклом по каждой заметке в словаре
        for note in self.notes_list:
            title = note.get_title()
            line = '-' * (len(title)+10)
            if list_parametr:
                print(f'{line}\n'
                      f"- {title} -\n"
                      f'{line}\n'
                      f'{note.get_data().strftime("%d %B %Y")}\n'
                      f'\n'
                      f'{note.get_text()}\n'
                      f'{line}\n')
            else:
                print(f'{line}\n'
                      f"- {title} -\n"
                      f'{line}\n'
                      f'\n'
                      f'{note.get_text()}\n'
                      f'{line}\n')

    # Функция вывода замтеок по указанным параметрам
    def parametrs_list_notes(self,parametr_id,parametr,show_data_parametr):
        parametr_notes_dict = {}
        position = 0
        if parametr_id == "1":
            if (suitable := 3 - parametr.count(None)) != 0:
                for note in self.notes_list:
                    counter = 0
                    if parametr[0]:
                        if note.get_data().day == parametr[0]:
                            counter += 1
                    if parametr[1]:
                        if note.get_data().month == parametr[1]:
                            counter += 1
                    if parametr[2]:
                        if note.get_data().year == parametr[2]:
                            counter += 1
                    if counter == suitable:
                        parametr_notes_dict[position := position + 1] = note
                        title = note.get_title()
                        line = '-' * (len(title) + 10)
                        print(f'{position}.\n'
                              f'  {line}\n'
                              f"  - {title} -\n"
                              f'  {line}\n'
                              f'  {note.get_data().strftime("%d %B %Y")}\n'
                              f'  \n'
                              f'  {note.get_text()}\n'
                              f'  {line}\n')
        elif parametr_id == "2":
            for note in self.notes_list:
                title = note.get_title()
                text = note.get_text()
                line = '-' * (len(title) + 10)
                if parametr.lower() in title.lower():
                    parametr_notes_dict[position := position + 1] = note
                    if show_data_parametr:
                        print(f'{position}.\n'
                              f'  {line}\n'
                              f"  - {title} -\n"
                              f'  {line}\n'
                              f'  {note.get_data().strftime("%d %B %Y")}\n'
                              f'  \n'
                              f'  {note.get_text()}\n'
                              f'  {line}\n')
                    else:
                        print(f'{position}.\n'
                              f'  {line}\n'
                              f"  - {title} -\n"
                              f'  {line}\n'
                              f'  \n'
                              f'  {note.get_text()}\n'
                              f'  {line}\n')
        else:
            for note in self.notes_list:
                title = note.get_title()
                text = note.get_text()
                line = '-' * (len(title) + 10)
                if parametr.lower() in text.lower():
                    parametr_notes_dict[position := position + 1] = note
                    if show_data_parametr:
                        print(f'{position}.\n'
                              f'  {line}\n'
                              f"  - {title} -\n"
                              f'  {line}\n'
                              f'  {note.get_data().strftime("%d %B %Y")}\n'
                              f'  \n'
                              f'  {note.get_text()}\n'
                              f'  {line}\n')
                    else:
                        print(f'{position}.\n'
                              f'  {line}\n'
                              f"  - {title} -\n"
                              f'  {line}\n'
                              f'  \n'
                              f'  {note.get_text()}\n'
                              f'  {line}\n')
        return parametr_notes_dict

    # Функция удаления заметоки
    def remove_note(self,id_note,notes_dict):
        self.notes_list.remove(notes_dict[id_note])

    # Функция редактирования заметки
    def edit_note(self,title, new_text):
        # Обновите словарь с новым текстом
        for note in self.notes_list:
            if note.get_title() == title:
                note.set_text(text=new_text)
                return True
        else:
            return False