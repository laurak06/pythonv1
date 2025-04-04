#   Built-in funcs

# map filter reduce zip enumerate

# zip - соединяет несколько последовательностей (получаем генератор, в котором элементы это tuple)

list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c']
list3 = [0.1, 5.5, 10.8, 0.5]

zipped = zip(list1, list2, list3)
print(list(zipped))

# enumerate - нумерует последовательность (по умолчанию с 0) (тоже получаем генератор)

enum = enumerate('hello', 1)
print(dict(enum))

for i in enum:
    print(i)

# map - принимает другую функцию и последовательность (записывает в новую последовательность результат функции, в которую передаются элементы)

list1 = ['1', '2', '3']
mapped = map(int, list1)

list2 = [1, 2, 3]
mapped = list(map(lambda x: x ** 2, list2))

# filter - возвращает генератор с элементами, прошедшими фильтрацию, принимает функцию и последовательность

list3 = ['hello', 'hi', '3', '4']
filtered = filter(str.isdigit, list3)
print(list(filtered))


print(list(filter(lambda x: x > 0, [1, 2, -5])))

# reduce - принимает функцию и последовательность, возвращает результат (передаваемая функция должна принимать 2 аргумента)

from functools import reduce

print(reduce(lambda x, y: x + y, [1, 2, 3, 4, 5])) 

# задачи 

# ZIP

list1 = [1, 2, 3, 4]
list2 = ['a', 'b', 'c', 'd']

# возведите во 2 степень числа из list1
# сделайте строки верхним регистром в list2
# сделайте dict при помощи zip и этих двух листов

mapped1 = list(map(lambda x: x ** 2, list1))
mapped2 = list(map(str.upper, list2))
zipped1 = dict(zip(mapped1, mapped2))

print(mapped1)
print(mapped2)
print(zipped1)

list1 = [1, 2, 3, 4, 5]
list2 = [1, 3, 3, 0, 5]

zipped = [x[0] == x[1] for x in zip(list1, list2)]
print(zipped)

lst = ['aza', '1234', '00']

filtered = list(filter(lambda x: x == x[::-1], lst))

s = ['1', '2', '3']
s1 = reduce(lambda x, y: f'{x}, {y}', s)
print(s1)