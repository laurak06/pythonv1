#1

class Document:

    def __init__(self, name):
        self.name = name

    def print_info(self):
        print('какой-то документ')


class PDFDocument(Document):
    def print_info(self):
        print(f'pdf документ {self.name}')


class WordDocument(Document):
    def print_info(self):
        print(f'word документ {self.name}')


docs = [PDFDocument('первый'), WordDocument('второй'), PDFDocument('третий')]

for doc in docs:
    doc.print_info()

#2

class Animal:
    def make_sound(self):
        pass


class Dog(Animal):
    def make_sound(self):
        print('гав')


class Cat(Animal):
    def make_sound(self):
        print('мяу')


class Cow(Animal):
    def make_sound(self):
        print('му')


def make_animals_talk(animals: list):
    for animal in animals:
        animal.make_sound()


make_animals_talk([Dog(), Cat(), Cow()])

#3

class Toy:
    def play_sound(self):
        pass


class Car(Toy):
    def play_sound(self):
        print('врум врум')


class Doll(Toy):
    def play_sound(self):
        print('ляллялялляля')


class Drum(Toy):
    def play_sound(self):
        print('бадум тсс')


toys = [Car(), Drum(), Doll()]
for toy in toys:
    toy.play_sound()


#4
from math import pi, sin


class Shape:
    def area(self):
        return pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def area(self):
        return self.x * self.y


class Triangle(Shape):
    '''сделала для прямоугольного'''
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        return (self.a * self.b) / 2


for shape in [Circle(2), Rectangle(2, 4), Triangle(3, 4, 5)]:
    print(shape.area())

#5
class Card:
    def __init__(self, amount):
        self.amount = amount

    def withdraw(self, amount):
        pass


class CreditCard(Card):
    def withdraw(self, amount):
        self.amount -= amount


class DebitCard(Card):
    def withdraw(self, amount):
        if self.amount >= amount:
            self.amount -= amount