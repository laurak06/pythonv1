# 1) Вы работаете в Банке и пишите программу которая считает % для кредита. Спросите у пользователя сумму займа(не меньше 100 000) и посчитайте сколько нужно будет вернуть если процент = 7.89, результат округлите до 2 чисел после точки.

#     Формула подсчёта переплаты: Сумма * (% / 100)

# def get_percent_for_loans(user_summa, percents):
#     return round(user_summa * (percents / 100), 2)

    
# user_summa = float(input('Введите сумму кредита (не меньше 100 000): ').replace(',', '.'))

# if user_summa >= 100000:
#     print(get_percent_for_loans(user_summa, 7.89))
# else:
#     print('слишком маленькая сумма')

#     2) Запросите у пользователя ввести текст с цифрами, 
#     найти цифры и преобразовать их в целое число, затем вывести на терминал

# def get_numbers():
#     string = input('enter string with numbers: ')
#     for i in string:
#         if i.isdigit():
#             print(int(i), end=' ')

# get_numbers()

#     3) Создайте  функцию, которая выполняет следующее действие:
#     Пользователь вводит количество месяцев и лет. 
#     Вывести в терминал количество дней за это время. 
#     Считать, что в каждом месяце 30 дней

# def get_days():
#     months = int(input('enter months: '))
#     years = int(input('enter years: '))
#     return (months + years * 12) * 30

# print(get_days())

#     4) Создайте функцию, которая возвращает словарь, 
#     где ключами будут числа от 1 до 10, а значениями эти же числа, возведенные в куб

# def get_dict_cubes():
#     return {i: i ** 3 for i in range(1, 11)}

#     5) Напишите функцию, которая высчитывает сумму чисел от 1 до 50 и возвращает результат. 

# def sum_50():
#     return sum(range(1, 51))
# print(sum_50())



# users = []

# # register: login and 2 passwords

# def register():
#     username = input('Введите ник: ')
#     password1 = input('Введите пароль: ')
#     password2 = input('Введите пароль еще раз: ')
#     user = {
#         'username': username,
#         'password1': password1,
#         'password2': password2
#     }
#     users.append(user)
#     print('Данные были успешно добавлены!')

# # login: username если есть тогда password

# def log_in():
#     username = input('Введите ник: ')
#     if users:
#         for i in users:
#             if username == i['username']:
#                 password = input('Введите пароль: ')
#                 if password == i['password1']:
#                     print('Добро пожаловать!')
#                 else:
#                     print('Вы ввели неверный пароль')
#                 break
#         else:
#             print('Такого пользователя нет в базе')


# def main():
#     while True:
#         print('1. Регистрация\n2. Войти\n3. Выйти')
#         answer = input('Ваш выбор: ').strip()
#         if answer == '1':
#             register()
#         elif answer == '2':
#             log_in()
#         elif answer == '3':
#             print('До свидания')
#             break
#         else:
#             print('Неверный выбор')

# main()


# plus = lambda x, y: x + y
# minus = lambda x, y: x - y
# multiply = lambda x, y: x * y
# division = lambda x, y: x / y
# degree = lambda x, y: x ** y

# def main():
#     while True:
#         print('Calculator')
#         try:
#             operator = input('enter operation(# if want to quit): ')
#             if operator == '#':
#                 break
#             num1 = float(input('enter 1 number: '))
#             num2 = float(input('enter 2 number: '))
#             if operator == '+':
#                 print(plus(num1, num2))
#             elif operator == '-':
#                 print(minus(num1, num2))
#             elif operator == '*':
#                 print(multiply(num1, num2))
#             elif operator == '/':
#                 print(division(num1, num2))
#             elif operator == '^':
#                 print(degree(num1, num2))
#             else:
#                 print('Такого оператора нет!')
#         except ValueError:
#             print('only umbers!')
#         except ZeroDivisionError:
#                 print('no zero division!')

        

# main()
