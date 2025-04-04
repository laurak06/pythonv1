#            ~Функции~
# функции - именнованный блок кода, который может принимать аргументы и возвращать результат

def my_sum(x, y):
    return x + y

def my_len(posl):
    count = 0
    for _ in posl:
        count += 1
    return count

#           ~виды параметров~
# 1 обязательные
# 2 необязательные (параметры):
#   3 дефолтные (аргументы)
#   4 *args - позиционные аргументы, которые не попали в обязательные и с дефолтом
#   5 **kwargs - все лишние именованные аргументы

def func_(x, y, z):
    return x + y + z


#           ~виды аргументов~
# 1 позиционные
# 2 именованные

def func(a, b=10, *args, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)

func()

