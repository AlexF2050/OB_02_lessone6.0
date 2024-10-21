
class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name

    def get_id(self):
        return self.user_id

    def get_name(self):
        return self.name

    def __repr__(self):
        return f'User(id={self.get_id()}, имя={self.get_name()})'


class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self.access_level = None
        self.users = []  # Список пользователей, которыми управляет администратор

    def set_access_level(self, access_level):
        self.access_level = access_level

    def get_access_level(self):
        return self.access_level

    def add_user(self, user):
        self.users.append(user)
        print(f'Пользователь {user.get_name()} добавлен.')

    def remove_user(self, user):
        if user in self.users: # Если пользователь есть в списке
            self.users.remove(user)
            print(f'Пользователь {user.get_name()} удален.')
        else:
            print(f'Пользователь {user.get_name()} не найден в списке.')

    def __repr__(self):
        return f'Admin(id={self.get_id()}, имя={self.get_name()}, уровень доступа={self.get_access_level()})'


# Пример использования

user = User('12345', 'Иван Петров')  # Присваиваем данные о пользователе (id, name)
admin = Admin('888', 'Лия Строгая')  # Присваиваем данные о пользователе (id, name)
admin2 = Admin('555', 'Павел Павлов')  # Присваиваем данные о пользователе (id, name)

print(user)  # Выводим данные о user
print(' ')

print(admin)  # Выводим данные о admin
print(' ')

print('Устанавливаем уровень доступа пользователя:')
admin.set_access_level('admin')  # Устанавливаем уровень доступа пользователя (access_level)
print(admin)
print(' ')

admin.add_user(admin2)  # Добавляем пользователя в список
print(admin2)
print(' ')

admin.remove_user(user)  # Пытаемся удалить пользователя из списка
print(admin)  # Выводим данные о администрато