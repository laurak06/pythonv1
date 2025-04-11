'================Абстракция==================='
# Абстракция - это принцип ООП, в котором мы создаем класс пустышку,
# где задаем названия атрибутов и методов, для того, чтобы в дочерних
# классах не забыть их переопределить

from abc import ABC, abstractmethod, abstractproperty


class AbstractAnimal(ABC):
    # @abstractproperty
    @property
    @abstractmethod
    def legs(self):
        ...

    @abstractmethod
    def voice(self):
        ...


class Dog(AbstractAnimal):
    legs = 4

    def voice(self):
        print('гав гав')


dog = Dog()

# Задания

# Наследование
# 1.1. Создайте базовый класс `Transport` с методом `move()`. Создайте два класса-наследника: `Car` и `Bike`, переопределите метод `move()` для каждого из них.

class Transport:
    def move(self):
        ...


class Car(Transport):
    def move(self):
        print('машина едет')


class Bike(Transport):
    def move(self):
        print('байк едет')

# 2.2. Создайте класс `Employee` с атрибутами `name` и `salary`. Создайте класс `Manager`, унаследованный от `Employee`, добавьте атрибут `department` и метод `show_info()`.
class Employee:
    name = 'Katana'
    salary = '100000$'


class Manager(Employee):
    department = 'KATANA'
    def show_info(self):
        print(super().name, super().salary, self.department)

# Инкапсуляция
# 3.1. Создайте класс `BankAccount` с приватным атрибутом `_balance`. Реализуйте методы `deposit()`, `withdraw()` и `get_balance()` для управления балансом.

# 4.2. Создайте класс `Student` с приватными полями `name` и `grade`. Реализуйте методы доступа (геттеры и сеттеры) с проверкой допустимости оценки (0–100).
class Student:
    def __init__(self, name, grade):
        self.__name = name
        self.__grade = grade

    @property
    def name(self):
        return self.__name

    @name.setter
    def set_name(self, name):
        self.__name = name

    @property
    def grade(self):
        return self.__grade

    @grade.setter
    def set_grade(self, grade):
        if 0 <= grade <= 100:
            self.__grade = grade
        else:
            print('оценка должна быть 0–100')
# Полиморфизм
# 5.1. Создайте классы `Dog` и `Cat`, каждый с методом `speak()`, возвращающим соответствующий звук. Создайте функцию `make_sound(animal)`, которая вызывает метод `speak()` независимо от типа животного.
class Dog:
    def speak(self):
        return 'гав'

class Cat:
    def speak(self):
        return 'мяу'


def make_sound(animal):
    print(animal.speak)

# 6.2. Создайте базовый класс `Shape` с методом `area()`. Создайте классы `Rectangle` и `Circle`, реализующие метод `area()` по-своему. Используйте цикл для вычисления площадей разных фигур.

