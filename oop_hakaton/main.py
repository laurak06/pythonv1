from mixins import RegisterMixin, LoginMixin, ChangePasswordMixin, ChangeUsernameMixin, CheckOwnerMixin


class User(RegisterMixin, LoginMixin, ChangePasswordMixin, ChangeUsernameMixin):
    pass


class Post(CheckOwnerMixin):
    def __init__(self, title, description, price, quantity, owner):
        if self.check(owner):
            self.title = title
            self.description = description
            self.price = price
            self.quantity = quantity
            self.owner = owner
            print('Successfully created!')
        else:
            print('Не получилось создать')


#тестирование класса User: login and register

users = User()
print(users.register('лаура', '12345678'))
print(users.register('lau', '12345678'))
print(users.register('katana', '123'))
print(users.register('katana', '00000000'))
print(users.login('lau', '12345678'))
print(users.login('lauk', '12345678'))
print(users.login('lau', 100))
print(users.register('laura', '123456789'))

#тестирование класса User: change_name and change_password

print(users.change_name('laura', 'nikita'))
print(users.change_name('noname1', 'noname2'))
print(users.change_password('lau', '12345678', '87654321'))
print(users.change_password('noname', '12345678', '87654321'))
print(users.change_password('lau', '12345678', '87654321'))


# тестирование класса Post

post1 = Post('first', 'just description', 1000, 5, 'lau')
post2 = Post('second', 'just description', 3000, 10, 'katana')
post3 = Post('third', 'ошибочный', 500, 3, 'noname')

