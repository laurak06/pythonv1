# 1. Создайте файл data.json с произвольными данными.
# Напишите программу, которая загружает его содержимое в Python-объект и выводит на экран
import json
# with open('data.json') as file:
#     data = json.load(file)
#     print(data)


# 2) Создайте словарь с данными о пользователе (name, age, email).
# Запишите его в файл user.json

# dict1 = {
#     'name': 'Laura',
#     'age': 18,
#     'email': 'lau@gmail.com'
# }
# with open('user.json', 'w') as file:
#     json.dump(dict1, file)


# # 3) Дана JSON-строка:
# # '{"product": "Laptop", "price": 1200, "in_stock": true}'
# # Преобразуйте ее в Python-словарь и выведите значение ключа "price".

# s = '{"product": "Laptop", "price": 1200, "in_stock": true}'
# dict2 = json.loads('{"product": "Laptop", "price": 1200, "in_stock": true}')
# print(dict2.get('price'))

# 4) Дан файл products.json с массивом товаров (id, name, price).
# Напишите функцию, которая принимает id товара и возвращает его данные.
# [
#   {"id": 1, "name": "Laptop", "price": 1200},
#   {"id": 2, "name": "Smartphone", "price": 800},
#   {"id": 3, "name": "Tablet", "price": 500}
# ]

# with open('products.json', 'w') as file:
#     json.dump([
#   {"id": 1, "name": "Laptop", "price": 1200},
#   {"id": 2, "name": "Smartphone", "price": 800},
#   {"id": 3, "name": "Tablet", "price": 500}
# ], file)
    
# def func1(item_id):
#     with open('products.json') as file:
#         for i in json.load(file):
#             if i.get('id') == item_id:
#                 return f"ID: {i.get('id')}\nИмя: {i.get('name')}\nЦена: {i.get('price')}"

        
# print(func1(2))

# 5) Дан config.json с настройками программы:
# {
#   "theme": "light",
#   "language": "en",
#   "volume": 70
# }
# Напишите функцию, которая изменяет переданный параметр (например, theme → "dark") и сохраняет изменения.

# with open('config.json', 'w') as file:
#     json.dump({
#   "theme": "light",
#   "language": "en",
#   "volume": 70
# }, file) 
    
# def remake(key, value):
#     with open('config.json', 'r') as file:
#         d = json.load(file)
#         if d.get(key):
#             with open('config.json', 'w') as file:
#                 d[key] = value
#                 json.dump(d, file)
        


# remake('them', 'dark')

# 6) Дан students.json, содержащий список студентов с их баллами.
# Напишите функцию, которая фильтрует студентов с баллом выше 80 и сохраняет их в top_students.json.
# [
#   {"name": "Alice", "score": 85},
#   {"name": "Bob", "score": 78},
#   {"name": "Charlie", "score": 90},
#   {"name": "Dave", "score": 65}
# ]

# with open('students.json', 'w') as file:
#     json.dump([
#   {"name": "Alice", "score": 85},
#   {"name": "Bob", "score": 78},
#   {"name": "Charlie", "score": 90},
#   {"name": "Dave", "score": 65}
# ], file) 
    
# def w_top_students():
#     with open('students.json') as file:
#         data = json.load(file)
#         top_students = []
#         for i in data:
#             if i.get('score') > 80:
#                 top_students.append(i)
#     with open('top_students.json', 'w') as file:
#         json.dump(top_students, file)


# w_top_students()

# 7) Есть два файла: employees1.json и employees2.json, содержащие списки сотрудников.
# Напишите программу, которая объединяет их в один список и сохраняет в all_employees.json, исключая дубликаты

# employees1.json:
# [
#   {"id": 1, "name": "John Smith", "department": "HR"},
#   {"id": 2, "name": "Jane Doe", "department": "IT"}
# ]

# employees1.json:
# [
#   {"id": 2, "name": "Jane Doe", "department": "IT"},
#   {"id": 3, "name": "Emily Johnson", "department": "Marketing"}
# ]

def merge_files(file_1, file_2):
    with open(file_1, 'r') as file1, open(file_2, 'r') as file2:
        file1_data = json.load(file1)
        file2_data = json.load(file2)
        all_users = {}
        for i in file1_data + file2_data:
            all_users[i['id']] = i
    with open('all_employees.json', 'w') as file:
        json.dump(list(all_users.values()), file)

merge_files('/Users/laura/Desktop/PythonV1/parsing/employees1.json', '/Users/laura/Desktop/PythonV1/parsing/employees2.json')

# 8) Создайте log.json, в который можно записывать события вида:
# {"timestamp": "2025-03-10 12:30:45", "event": "User logged in", "user_id": 123}
# Напишите функцию log_event(event, user_id), которая добавляет новую запись в этот файл.


# from datetime import datetime


# def log_event(event, user_id):
#     log_entry = {
#         "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
#         "event": event,
#         "user_id": user_id
#     }
#     try:
#         with open('log.json', 'r') as file:
#             logs = json.load(file)
#     except FileNotFoundError:
#         logs = [] 

#     logs.append(log_entry)
#     with open('log.json', 'w') as file:
#         json.dump(logs, file)


# log_event('hiii', 20)