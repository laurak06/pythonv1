'=================Миксины===================='
# Миксины - это классы, которые будут использоваться для наследования.
# Но от миксинов не создаются объекты. Классы помощники

class FlyMixin:
    def fly(self):
        print('я могу летать')

class WalkMixin:
    def walk(self):
        print('я могу ходить')

class SwimMixin:
    def swim(self):
        print('я могу плавать')

class Human(WalkMixin, SwimMixin):
    name = 'человек'

    def talk(self):
        print('я могу говорить')

class Fish(SwimMixin):
    name = 'рыба'

class Duck(WalkMixin, SwimMixin, FlyMixin):
    name = 'утка'


objects = [Human(), Fish(), Duck()]

for obj in objects:
    attrs = ['fly', 'swim', 'walk', 'talk']
    for attr in attrs:
        if hasattr(obj, attr):
            method = getattr(obj, attr)
            method()

obj = Human()
setattr(obj, 'name', 'katana')

# hasattr = функция, которая принимает обьект и название аттрибута
# возвращает True если есть такой аттрибут

# getattr - функция, которая принимает обьекты и названия аттрибута, возвращает значение аттрибута

# setattr - функция, которая принимает обьект, название аттрибута, значение для этого аттрибута
# добавляет в обьект новый аттрибут или перезаписывает одноименный аттрибут