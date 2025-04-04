'=============OOP==========='
# парадигма

# class - это шаблон
# object(instance, экземпляр) - конечный продукт класса

class Person:
    arms = 2
    legs = 2

    def __init__(self, name, age, profession):
        self.name = name
        self.age = age
        self.profession = profession

    def walk(self):
        print(f'{self.name} ходит')

    def swim(self):
        print(f'{self.name} плавает')


obj1 = Person('Katana', 21, 'dev')
obj2 = Person('Nick', 21, 'dev')
obj3 = Person('Laura', 20, 'senior dev')

obj1.walk()
obj1.swim()
obj2.swim()