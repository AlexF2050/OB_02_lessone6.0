# Этот class Bird() будет Базовым (родителем)  для class Pigeon()

#_____Этот class Bird() будет Базовым (родителем)  для class Pigeon() _______________________________________________

class Bird(): # bird class
    def __init__(self, name, voice, color): # bird constructor создаем переменные и инициализируем их значения
        self.name = name # создаем характеристики
        self.voice = voice
        self.color = color

    # Задаём, что может делать птица, какие методы будут вызываться при создании объекта
    def fly(self): # метод полета
        print(f"{self.name} - летает")

    def eat(self): # метод еды
        print(f"{self.name} - кушает") # выводим сообщение

    def sing(self): # метод пения
        print(f"{self.name} - поёт - чирик {self.voice}") # выводим сообщение

    def info(self): # метод вывода информации
        print(f"{self.name} - имя") # выводим сообщение
        print(f"{self.voice} - голос") # выводим сообщение
        print(f"{self.color} - цвет") # выводим сообщение

#_____Этот class Pigeon() будет производным для Этот class Bird()  _______________________

class Pigeon(Bird): # наследуемся от класса Bird
    def __init__(self, name, voice, color, favorite_food): # вызываем из базового класса Bird, всё что есть в базовом классе Bird - характеристики
        super().__init__(name, voice, color) # вызываем из базового класса Bird, всё что есть в базовом классе Bird - характеристики
        self.favorite_food = favorite_food

    def sing(self): # метод пения
        print(f"{self.name} - поёт - курлык курлык")

    def walk(self):
        print(f"{self.name} - ходит") # выводим сообщение


bird1 = Pigeon( "Гоша", "Курлы", "белый", "семена") # создание объекта

bird2= Bird("Маша", "Синица", "синий") # создание объекта

bird1.sing() # вызываем метод
bird1.info() # вызываем метод