'===========Ассоциация============'
# Ассоциация - это принцип ООП, в котором 2 класса связаны друг с другом

'композиция' #сильная связь
'агрегация' #слабая связь

class Battery:
    _power = 100

    def charge(self):
        if self._power < 100:
            self._power = 100

# композиция
class Iphone:
    def __init__(self, color):
        self.color = color
        self.battery = Battery()

# агрегация
class Nokia:
    def __init__(self, color, battery):
        self.color = color
        self.battery = battery


iphone = Iphone('deep purple')
battery_for_nokia = Battery()
nokia = Nokia('black', battery_for_nokia)