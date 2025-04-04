    # 1) Создайте файл, внесите туда небольшой текст. В программе откройте этот файл и выведите содержимое на экран.

with open('dz/text.txt', 'r') as file:
    print(file.read())

    # 2)Создайте файл users.txt. Напишите программу которая спрашивает у пользователя его Логин и Пароль и
    # записывает в файл users.txt.

with open('dz/users.txt', 'w') as file:
    login = input('enter login: ')
    password = input('enter password: ')
    file.write(f'Login: {login}\n')
    file.write(f'Password: {password}')


    # 3) Создайте программу, которая считает из файла текст, и если в тексте содержится буква “w”, то выведет на экран
    # “Да, в тексте есть w”, иначе - “Нет, в тексте нет w”. Подсказка: используйте ключевое слово in.

with open('dz/text.txt', 'r') as file:
    if 'w' in file.read():
        print('Да')
    else:
        print('Нет')

    # 4) Создайте текстовый файл python.txt и запишите в него следующий текст:
    # """
    # Next, install the Python 3 interpreter on your computer. This is the program that reads Python programs and carries out their instructions;
    # you need it before you can do any Python programming. Mac and Linux distributions may include an outdated version of Python (Python 2),
    # but you should install an updated one (Python 3). See BeginnersGuide/Download for instructions to download the correct version of Python.
    # """
    # Затем, считайте его. Найдите слова которые содержат букву  "o" и запишите в список o_words=[] и
    # выведите на экран все полученные слова.

with open('dz/python.txt', 'w') as file:
    file.write("""
    Next, install the Python 3 interpreter on your computer. This is the program that reads Python programs and carries out their instructions;
    you need it before you can do any Python programming. Mac and Linux distributions may include an outdated version of Python (Python 2),
    but you should install an updated one (Python 3). See BeginnersGuide/Download for instructions to download the correct version of Python.
    """)
with open('dz/python.txt', 'r') as file:
    o_words=[]
    for i in file:
        for k in i.split():
            if 'o' in k:
                o_words.append(k.replace(',', '').replace('.', '').replace('(', '').replace(')', ''))

print(', '.join(o_words))

    # 5) Возьмите следующий текст:
    # """
    # .detacilpmoc naht retteb si xelpmoC
    # .xelpmoc naht retteb si elpmiS
    # .ticilpmi naht retteb si ticilpxE
    # .ylgu naht retteb si lufituaeB
    # """
    # Запишите его в файл. Далее считайте этот текст с файла и выведите в обратном порядке.

with open('dz/new.txt', 'w+') as file:
    file.write("""
    .detacilpmoc naht retteb si xelpmoC
    .xelpmoc naht retteb si elpmiS
    .ticilpmi naht retteb si ticilpxE
    .ylgu naht retteb si lufituaeB
    """)
    file.seek(0)
    content = file.read()

print(content[::-1])


    # 6) Создайте файл и запишите туда следующий текст:
    # """
    # 123
    # aaa456
    # fxdya 5 0 0
    # """
    # В каждой строчке есть цифры, которые вместе дадут число.
    # Посчитайте сумму всех чисел.

with open('dz/digits.txt', 'w') as file:
    file.write("""
    123
    aaa456
    fxdya 5 0 0
    """)

with open('dz/digits.txt', 'r') as file:
    content = file.read()

# 1 вариант
summa = (content.count('1') + content.count('2') * 2
         + content.count('3') * 3 +  content.count('4') * 4
         + content.count('5') * 5 + content.count('6') * 6
         + content.count('7') * 7 + content.count('8') * 8
         + content.count('9') * 9)

print(summa)

# 2 вариант
summa = 0
for i in content:
    if i.isdigit(): 
        summa += int(i)

print(summa)