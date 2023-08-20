#Класс создания заметки
class Note:
    #Констпруктор класса
    def __init__(self,title,text,data):
        self.title = title
        self.text = text
        self.data = data

    # Функция установки заголовка заметки
    def set_title(self,title):
        self.title = title

    # Функция установки текста заметки
    def set_text(self,text):
        self.text = text

    # Функция установки даты заметки
    def set_data(self,data):
        self.data = data

    # Функция получения заголовка заметки
    def get_title(self):
        return self.title

    # Функция получения текста заметки
    def get_text(self):
        return self.text

    # Функция получения даты заметки
    def get_data(self):
        return self.data

    # Функция получения всех переменных
    def get_all(self):
        return [self.title,self.text,str(self.data)]