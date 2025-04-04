'функции внешнего порядка'

# функции высшего порядка - это функции которые принимают в аргументы другую функцию
# создают функции внутри себя вызывает функцию и возвращает функцию

# def func_1(x):
#     ...

# def func_2():
#     ...

# func_1(func_2)
'------------------'
# def func_1():
#     ...
#     def func_2():
#         ...
'------------------'
# def func_1():
#     ...

# def func_2():
#     ...
'------------------'

# def func_1():
#     print('hi')
#     return func_1
# func_1()

'--------Декораторы------------'

# декоратор - функция высшего порядка, которая нужна, чтобы расширить функционал другой функции, не изменяя ее (функция обертка)


def glushitel(func):
    def wrapper(*args, **kwargs):
        print('тихааа')
        func()
    return wrapper

@glushitel
def automat():
    print('piuuu')

@glushitel
def gun():
    print('стрелять')

glushitel(gun)()
glushitel(automat)()
