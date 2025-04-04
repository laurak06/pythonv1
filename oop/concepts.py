'=================Принципы ООП================='
# Наследование
# Инкапсуляция
# Полиморфизм
# Абстракция
# Ассоциация (Агрегация, Композиция)


'==============Наследование================'
# Наследование - принцип ООП, в котором мы можем унаследовать, переопределить и использовать
# в дочернем классе все методы и аттрибуты родительского класса

class A:
    def method(self):
        print('method class A')


obj_a = A()

obj_a.method()

class B(A):
    pass

obj_b = B()
obj_b.method()

class C(A):
    def method(self):
        print('method class C')

obj_c = C()
obj_c.method()


class Animal:
    price = 100000
    def voice(self):
        ...

class Dog(Animal):
    def voice(self):
        return 'woof'

class Cat(Animal):
    def voice(self):
        return 'meow'

class Duck(Animal):
    def voice(self):
        return 'krya'

Bobik = Dog()
Barsik = Cat()
Donald = Duck()

# одиночное наследование
class A:
    ...

class B(A):
    ...

# иерархическое наследование (1 родитель, много дочерних)

class A:
    ...

class B(A):
    ...

class C(A):
    ...

# множественное наследование

class A:
    ...

class B:
    ...

class C(A, B):
    ...

# многоуровневое наследование

class A:
    ...

class B(A):
    ...

class C(B):
    ...

class D(C):
    ...

# гибридное наследование

class A:
    ...
class B(A):
    ...
class C(A):
    ...
class E:
    ...
class D(C, E):
    ...