# Инкапсуляция — это механизм объектно-ориентированного программирования, работа которого заключается в сокрытии
# деталей реализации, а также в объединении данных и методов, работающих с этими данными в единый класс (компонент),
# с целью предотвращения непреднамеренного изменения данных.

class Test(): #test class
    def __init__(self): # создание объекта
        self.public = "1 публичный атрибут" #публичный атрибут
        self._protected = "2 защищенный атрибут" #защищенный атрибут ОДНО подчеркивание _protected
        self.__private= "3 приватный атрибут" #приватный атрибут ДВА подчеркивания __private

# getter получение приватного атрибута
    def get_private(self): #доступ к приватному атрибуту
        return self.__private # возвращаем приватный атрибут

# setter установка нового значения приватного атрибута
    def set_private(self , value): #установка нового значения приватного атрибута - ценность
        self.__private = value # устанавливаем новое значение приватного атрибута - ценность

test = Test() # создание объекта класса Test
# достаём из публичного атрибута значение атрибута
print(test.public) #публичный атрибут выводим на экран

print(test._protected) #защищенный атрибут выводим на экран - НО лучше этого не делать

##print(test.__private) #приватный атрибут НЕ ДАЁТ выводить на экран - и не надо, если надо то применяем отдельные функции
# ниже правильный вариант вызова функции и вывода на экран
print(test.get_private()) #вызываем функцию get_private и выводим на экран

# Заменяем 3  и устанавливаем новое значение 4 приватного атрибута -
test.set_private("4 получили значение приватного атрибута") #устанавливаем новое значение приватного атрибута

print(test.get_private()) #вызываем функцию get_private и выводим на экран
