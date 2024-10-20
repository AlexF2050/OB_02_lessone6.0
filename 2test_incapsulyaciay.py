class Test():
    def public_function(self):
        print("1 Публичная функция - метод") # public_function

    # создаём защищённый метод
    def _protected_function(self): # _ - защищённый метод
        print("2 Защищённая функция - метод") # protected_function

    # создаём приватную функцию (за пределами класса она недоступна и работает только внутри класса)
    def __private_function(self):
        print("3 Приватная функция - метод") # private_function

# !!! напрямую мы не можем вызывать метод private_function поэтому используем test_private_function
    def test_private_function(self):
        self.__private_function() # вызываем метод private_function

test = Test() # создаём объект
test.public_function() # вызываем метод public_function
test._protected_function() # вызываем метод protected_function

##test.__private_function() #напрямую мы не можем вызывать метод private_function поэтому используем test_private_function
test.test_private_function() # вызываем метод private_function
