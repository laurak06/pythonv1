# 1. Абстрактный транспорт
# Создай абстрактный класс Transport с абстрактным методом move(). Реализуй два
# класса Car и Plane, которые наследуются от Transport и реализуют метод move() по-
# своему.
# Пример вывода:
# Car is moving on the road
# Plane is flying in the sky

from abc import ABC, abstractmethod


# class Transport(ABC):
#     @abstractmethod
#     def move(self):
#         '''Абстрактный метод'''
#         pass
#
# class Car(Transport):
#     def move(self):
#         return 'Car is moving on the road'
#
# class Plane(Transport):
#     def move(self):
#         return 'Plane is flying in the sky'
#
# 2. Платёжная система
# Создай абстрактный класс PaymentMethod с методом pay(amount). Сделай классы
# CreditCard и PayPal, реализующие этот метод с выводом способа оплаты и суммы.
# Пример вывода:
# Оплата 1000 через Credit Card
# Оплата 500 через PayPal

# class PaymentMethod(ABC):
#     @abstractmethod
#     def pay(self, amount):
#         pass
#
#
# class CreditCard(PaymentMethod):
#     def pay(self, amount):
#         return f'Оплата {amount} через Credit Card'
#
#
# class PayPal(PaymentMethod):
#     def pay(self, amount):
#         return f'Оплата {amount} через PayPal'
#
# 3. Фигуры и площадь
# Создай абстрактный класс Shape с методом area(). Реализуй классы Circle и Rectangle с
# соответствующим вычислением площади.
# Пример вывода:
# Площадь круга: 78.5
# Площадь прямоугольника: 200
# from math import pi


# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
#
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#
#     def area(self):
#         return pi * self.radius ** 2
#
# class Rectangle(Shape):
#     def __init__(self, weight, height):
#         self.weight = weight
#         self.height = height
#
#     def area(self):
#         return self.height * self.weight
#
# 4. Устройства вывода
# Определи абстрактный класс OutputDevice с методом display(text). Создай Monitor и
# Printer, которые выводят текст по-разному (например, просто через print, но с
# разными префиксами).
# Пример вывода:
# [Monitor] Hello, world!
# [Printer] Hello, world!

# class OutputDevice(ABC):
#     @abstractmethod
#     def display(self, text):
#         pass
#
# class Monitor(OutputDevice):
#     def display(self, text):
#         print(f'[Monitor] {text}')
#
# class Printer(OutputDevice):
#     def display(self, text):
#         print(f'[Printer] {text}')

#
# 5. Абстрактный животный класс
# Создай абстрактный класс Animal с методом make_sound(). Создай два класса Dog и
# Cat, которые реализуют этот метод (выводят «Гав!» и «Мяу!» соответственно).
# Пример вывода:
#
# Гав!
# Мяу!
#
# class Animal(ABC):
#     @abstractmethod
#     def make_sound(self):
#         pass
#
# class Dog(Animal):
#     def make_sound(self):
#         return 'гав'
#
# class Cat(Animal):
#     def make_sound(self):
#         return 'мяу'

# 6. Абстрактный работник
# Определи класс Employee с методом calculate_salary(). Сделай Developer и Manager,
# возвращающие зарплату с разными расчётами (фикс + бонус, почасовая и т.п.).
# Пример вывода:
# Зарплата разработчика: 5000
# Зарплата менеджера: 7000

# class Employee(ABC):
#     @abstractmethod
#     def calculate_salary(self):
#         pass
#
# class Developer(Employee):
#     def __init__(self, hours, salary_per_hour):
#         self.hours = hours
#         self.salary_per_hour = salary_per_hour
#
#     def calculate_salary(self):
#         return self.hours * self.salary_per_hour
#
# class Manager(Employee):
#     def __init__(self, fix, perks):
#         self.fix = fix
#         self.perks = perks
#
#     def calculate_salary(self):
#         return self.fix * self.perks #perks будут проценты


#
# 7. Интерфейс базы данных
# Создай абстрактный класс Database с методами connect() и disconnect(). Реализуй
# классы MySQLDatabase и PostgreSQLDatabase, которые выводят информацию о
# подключении/отключении.
# Пример вывода:
# Подключение к MySQL
# Отключение от MySQL
# Подключение к PostgreSQL
# Отключение от PostgreSQL

# class Database(ABC):
#     @abstractmethod
#     def connect(self):
#         pass
#
#     @abstractmethod
#     def disconnect(self):
#         pass
#
# class PostgreSQLDatabase(Database):
#     def connect(self):
#         print('Подключение к MySQL')
#
#     def disconnect(self):
#         print('Отключение от MySQL')
#
#
# class MySQLDatabase(Database):
#     def connect(self):
#         print('Подключение к PostgreSQL')
#
#     def disconnect(self):
#         print('Отключение от PostgreSQL')
