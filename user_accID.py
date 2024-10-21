#Разработай систему управления учетными записями пользователей для небольшой компании.
# Компания разделяет сотрудников на обычных работников и администраторов.
# У каждого сотрудника есть уникальный идентификатор (ID), имя и уровень доступа.
# Администраторы, помимо обычных данных пользователей, имеют дополнительный уровень доступа
# и могут добавлять или удалять пользователя из системы.
#Требования:
#1. Класс User*: Этот класс должен инкапсулировать данные о пользователе: ID, имя и уровень доступа ('user' для обычных сотрудников).
#2. Класс Admin: Этот класс должен наследоваться от класса User. Добавь дополнительный атрибут уровня доступа,
# специфичный для администраторов ('admin'). Класс должен также содержать методы add_user и remove_user,
# которые позволяют добавлять и удалять пользователей из списка (представь, что это просто список экземпляров User).
#3. Инкапсуляция данных: Убедись, что атрибуты классов защищены от прямого доступа и модификации снаружи.
# Предоставь доступ к необходимым атрибутам через методы  public, _protected, __private и get и set методы.

#______________________Создание класса User___________________________________________________________________________

#('user' для обычных сотрудников, 'admin' для администраторов)
class User: # Инкапсулируем данные о пользователе (id, name, access_level)
    def __init__(self, user_id, name): # Инициализируем данные о пользователе (id, name)
        self.__user_id = user_id # приватный атрибут id !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        self.__name = name # имя пользователя
        self.__access_level = 'user' # уровень доступа обычного пользователя

    def get_user_id(self): # Возвращает идентификатор пользователя (id)
        return self.__user_id

    def get_name(self): # Возвращает имя пользователя (name)
        return self.__name

    def get_access_level(self): # Возвращает уровень доступа пользователя (access_level)
        return self.__access_level

    def set_access_level(self, access_level): # Устанавливает уровень доступа пользователя (access_level)
        self.__access_level = access_level

#______________________Создание производного класса Admin от User ___________________________________________________________________________

class Admin(User): # Инкапсулируем данные о пользователе (id, name, access_level)
    def __init__(self, user_id, name): # Инициализируем данные о пользователе (id, name)
        super().__init__(user_id, name) # Инициализируем данные о пользователе (id, name) из базового класса User super - означает наследование класса User
        self.__access_level = 'admin' # уровень доступа администратора

    def add_user(self, user_list, user): # Добавляем пользователя в список пользователей
        if isinstance(user, User): # Проверяем, является ли объект user объектом класса User
            user_list.append(user) # Добавляем пользователя в список пользователей
            print(f'Пользователь {user.get_name()} добавлен.')
        else:
            print('Только объекты класса User могут быть добавлены.')

    def remove_user(self, user_list, user): # Удаляем пользователя из списка пользователей
        if user in user_list: # Проверяем, есть ли пользователь в списке
            user_list.remove(user) # Удаляем пользователя из списка пользователей
            print(f'Пользователь {user.get_name()} удалён.')
        else:
            print('Пользователь не найден в списке.')

#______________________ Работа со списком пользователей______________________________________________________

# Создаём список пользователей
user_list = []

# Создаем обычных пользователей
user1 = User(1001, "Иван Дамов")
user2 = User(1002, "Марья Искусница")
user3 = User(1003, "Саша Усталов")
# Создаем администратора
admin = Admin(1010, "Сергей Весёлый")

# Администратор добавляет пользователей
admin.add_user(user_list, user1) # Добавляем пользователя в список пользователей
admin.add_user(user_list, user2) # Добавляем пользователя в список пользователей
admin.add_user(user_list, user3) # Добавляем пользователя в список пользователей

# Выводим список пользователей
print("\nСписок пользователей:")
for user in user_list:
    print(f'ID: {user.get_user_id()}, Имя: {user.get_name()}, Уровень доступа: {user.get_access_level()}')

# Администратор удаляет пользователя
admin.remove_user(user_list, user1)

# Выводим обновленный список пользователей
print("\nОбновленный список пользователей:")
for user in user_list:
    print(f'ID: {user.get_user_id()}, Имя: {user.get_name()}, Уровень доступа: {user.get_access_level()}')