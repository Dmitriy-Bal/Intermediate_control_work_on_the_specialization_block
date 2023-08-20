#Класс создания интерфейса программы
class Interface:
    # Констпруктор класса
    def __init__(self):
        pass

    # Главное меню
    def main_menu(self):
        self.clear()
        return input("Главное меню: \n"
              "  1.Создать заметку\n"
              "  2.Сохранить в файл\n"
              "  3.Извлечь из фала\n"
              "  4.Читать список заметок\n"
              "  5.Редактировать заметку\n"
              "  6.Удалить заметку\n"
              "  7.Выход\n"
                     "Ввод: ")

    # Меню просмотра заметок
    def watch_notes_menu(self):
        self.clear()
        while (out := input("1. По параметру\n"
                            "2. Весь список\n"
                            "Ввод: ")) not in ["1", "2"]:
            self.clear()
            print("Ошибка!\n")
            self.press_enter()
            self.clear()

        self.clear()
        return out == '1'

    # Меню параметров заметки
    def parametrs_menu(self):
        self.clear()
        while (out := input("1. По дате\n"
                            "2. По заголовку\n"
                            "3. По тексту\n"
                            "Ввод: ")) not in ["1", "2","3"]:
            self.clear()
            print("Ошибка!\n")
            self.press_enter()
            self.clear()

        self.clear()
        return out

    # Меню чтения заметки из файла
    def read_menu(self):
        self.clear()
        while (out := input("Добавить заметки к существующим?\n"
                           "1. Да\n"
                           "2. Нет\n"
                     "Ввод: ")) not in ["1","2"]:
            self.clear()
            print("Ошибка!\n")
            self.press_enter()
            self.clear()

        self.clear()
        return out == '1'

    # Меню отображения заметки
    def date_menu(self):
        self.clear()
        while (out := input("Показывать дату создания заметок?\n"
                     "1.Да\n"
                     "2.Нет\n"
                     "Ввод: ")) not in ["1","2"]:
            self.clear()
            print("Ошибка!\n")
            self.press_enter()
        self.clear()
        return out == '1'

    # Запрос заголовка от пользователя
    def title(self):
        self.clear()
        return input("Введите заголовок:\n")

    # Запрос даты от пользователя
    def data(self):
        self.clear()

        print("Вводите параметр в формате числа!"
              "Что бы пропустить параметр введите 0\n")

        while not (day := input("Введите день: ")).isdigit():
            print("Ошибка! Введите число!")
        while not (month := input("Введите месяц: ")).isdigit():
            print("Ошибка! Введите число!")
        while not (year := input("Введите год: ")).isdigit():
            print("Ошибка! Введите число!")

        return [int(day) if int(day) else None,int(month) if int(month) else None,int(year) if int(year) else None]

    # Запрос номера заметки от пользователя
    def choose_note(self):
        while not (value := input("Введите номер заметки: ")).isdigit():
            print("Ошибка! Введите число!")

        return int(value)

    # Запрос текста заметки от пользователя
    def text(self):
        self.clear()
        text = ""
        print("Вводите текст,для выхода напишите в пустой строке нажмите 'enter':\n")
        while (out := input()) != "":
            text += out +"\n"
        return text[:-1]

    # Запрос имени файла от пользователя
    def file_name(self):
        self.clear()
        return input("Введите имя файла:\n")

    # Ошибка поиска заметки
    def title_not_found(self):
        self.clear()
        return input("Заметка не найдена!\n"
                     "press enter ....")


    def press_enter(self):
        return input("\npress enter ....")


    def repeat_input(self):
        self.clear()
        print("Повторите ввод!")

    def error_find_note(self):
        self.clear()
        print("Ошибка! Заметка не найдена!")

    def error_exists_note(self):
        self.clear()
        print("Ошибка! Заметка существует!")

    def successfully_remove(self):
        self.clear()
        print("Заметка успешно удалена!")

    def seccess(self):
        self.clear()
        print("Успешно!")

    # Отчистка консоли
    def clear(self):
        for _ in range(100): print("\n")