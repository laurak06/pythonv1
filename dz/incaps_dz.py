# ИНКАПСУЛЯЦИЯ:
#     1) Создай класс BankAccount с приватным __balance. Добавь методы:
# 	    1) deposit(amount) – пополнение баланса
# 		2) withdraw(amount) – снятие (он должен снимать не больше текущего баланса)
# 		3) get_balance() – возвращает баланс

# class BankAccount:
#     def __init__(self):
#         self.__balance = 0
#
#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#             print('Пополнение завершилось')
#         else:
#             print('Пополнение должно быть больше 0')
#
#     def withdraw(self, amount):
#         if self.__balance >= amount:
#             self.__balance -= amount
#             print('Снятие завершилось')
#         else:
#             print('Недостаточно средств!')
#
#     def get_balance(self):
#         return self.__balance
#

#     2) Создай класс User в котором (задание по теме getters/setters):
# 		1) name — публичный атрибут
# 		2) password — приватный атрибут
# 		3) Метод get_password() который будет возвращать * вместо пароля
# 		4) Метод set_password(new_password), который будет проверять длину пароля,
#         и если она больше 6 символов, то меняет предыдущий на новый
#         ПРИМЕЧАНИЕ: пароль должен состоять из букв и цифр

class User:
    def __init__(self, name, password):
        self.name = name
        self.__password = password

    def get_password(self):
        return len(self.__password) * '*'

    def set_password(self, new_password):
        if len(new_password) > 6 and new_password.isalnum():
            self.__password = new_password
        else:
            print('пароль должен состоять из букв и цифр и больше 6 символов')

#     3) Создайте класс Employee у которого есть:
# 		1) name – имя сотрудника
# 		2) __salary (приватный атрибут)
# 		3) salary (геттер) – возвращает зарплату
# 		5) salary (сеттер) – изменяет зарплату (не меньше 30_000)

# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.__salary = salary
#
#     def get_salary(self):
#         return self.__salary
#
#     def set_salary(self, new_salary):
#         if new_salary >= 30000:
#             self.__salary = new_salary
#         else:
#             print('сумма должна быть не меньше 30_000')


# 4) Создайте класс Circle у которого есть:
# 	1) radius (геттер/сеттер, не < 0).
# 	2) area (геттер) – вычисляет площадь (число пи * радиус в квадрате).
#
#     Затем:
#
#     Создайте дочерний класс Cylinder(Circle) и добавьте в него:
# 	    1)height (геттер/сеттер, не < 0)

from math import pi


class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.area = pi * self.radius ** 2

    def get_radius(self):
        return self.area

    def set_radius(self, new_radius):
        if new_radius >= 0:
            self.radius = new_radius
        else:
            print('радиус должен быть не меньше 0')

    def get_area(self):
        return self.area


class Cylinder(Circle):
    def __init__(self, radius, height):
        super().__init__(radius)
        self.height = height

    def get_height(self):
        return self.height

    def set_height(self, new_height):
        if new_height >= 0:
            self.radius = new_height
        else:
            print('высота должна быть не меньше 0')

