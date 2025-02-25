# 1) Напишите декоратор, который перед вызовом функции будет выводить сообщение "Выполнение функции..."
# 2) Создайте декоратор, который будет умножать результат выполнения числовой функции на 2
# 3) Создайте декоратор, который к строковому результату функции добавляет "!" в конце
# 4) Создайте декоратор, который ограничит выполнение функции 3 вызовами
# Если функция вызывается больше 3 раз, выводить сообщение "Функция больше недоступна"
# 5) Создайте декоратор, который будет выводить переданные аргументы перед вызовом функции

# 1
def decorator1(func):
    def wrapper(*args, **kwargs):
        print("Выполнение функции...")
        func(*args, **kwargs)

    return wrapper

# 2
def decorator2(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs) * 2

    return wrapper

# 3
def decorator3(func):
    def wrapper(*args, **kwargs):
        return str(func(*args, **kwargs)) + '!'

    return wrapper

# 4
def decorator4(func):
    counter = 0
    def wrapper(*args, **kwargs):
        nonlocal counter
        if counter < 3:
            counter += 1
            return func(*args, **kwargs)
        else:
            print('Функция больше недоступна')

    return wrapper

# 5
def decorator5(func):
    def wrapper(*args, **kwargs):
        print(f'позиционные аргументы: {args}\nименованные:{kwargs}')
        func(*args, **kwargs)
    return wrapper