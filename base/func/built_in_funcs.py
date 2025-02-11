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