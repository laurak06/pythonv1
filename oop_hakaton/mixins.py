import json


class RegisterMixin:

    def register(self, name, password):
        try:
            with open('user.json', 'r') as file:
                users = json.load(file)
        except:
            users = []

        try:
            if name in {user['name'] for user in users}:
                raise Exception('Такой юзер уже существует!')

            if validate_password(password):
                new_user = {
                    'id': len(users),
                    'name': name,
                    'password': password
                }
                users.append(new_user)
                with open('user.json', 'w') as file:
                    json.dump(users, file, indent=4)
                    return 'Successfully registered'
            return 'Не получилось зарегистрироваться!'

        except Exception as error:
            return error


class LoginMixin:
    def login(self, name, password):
        with open('user.json', 'r') as file:
            users = json.load(file)
        try:
            for user in users:
                if user['name'] == name:
                    if user['password'] != password:
                        raise Exception('Неверный пароль!')
                    return 'Вы успешно залогинились!'
            return 'Нет такого юзера в БД!'

        except Exception as error:
            return error


class ChangePasswordMixin:
    def change_password(self, name, old_password, new_password):
        if validate_password(new_password):
            with open('user.json', 'r') as file:
                users = json.load(file)
            try:
                for user in users:
                    if user['name'] == name:
                        if user['password'] != old_password:
                            raise Exception('Старый пароль указан неверно!')

                        user['password'] = new_password
                        with open('user.json', 'w') as file:
                            json.dump(users, file, indent=4)
                        return 'Password changed successfully!'

                raise Exception('Нет такого юзера в БД!')
            except Exception as error:
                return error


class ChangeUsernameMixin:
    def change_name(self, old_name, new_name):
        with open('user.json', 'r') as file:
            users = json.load(file)
        user_names = {user['name'] for user in users}
        try:
            if old_name not in user_names:
                raise Exception('Нет такого зарегистрированного юзера в БД!')
        except Exception as error:
            return error

        while new_name in user_names:
            print('Пользователь с таким именем уже существует!')
            new_name = input('Введите новое имя:')

            for user in users:
                if user['name'] == old_name:
                    user['name'] = new_name

                    with open('user.json', 'w') as file:
                        json.dump(users, file, indent=4)

                    return 'Username changed successfully'


class CheckOwnerMixin:
    def check(self, owner):
        with open('user.json', 'r') as file:
            users = json.load(file)
        try:
            if owner not in {user['name'] for user in users}:
                raise Exception('Нет такого пользователя!')
            return True

        except Exception as error:
            print(error)
            return False


def validate_password(password: str):
    try:
        if len(password) < 8:
            raise Exception('Пароль слишком короткий!')
        if not password.isalnum():
            raise Exception('Пароль должен состоять из букв и цифр!')
        return True
    except Exception as error:
        print(error)
        return False