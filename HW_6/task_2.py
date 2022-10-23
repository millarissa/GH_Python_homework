"""
Створіть функцію для валідації пари ім'я/пароль
за наступними правилами:
   - ім'я повинно бути не меншим за 3 символа і
   не більшим за 50;
   - пароль повинен бути не меншим за 8 символів і
   повинен мати хоча б одну цифру;
   - пароль повинен мати хоча б одну велику літеру
   Якщо якийсь із параметрів не відповідає вимогам -
   породити виключення із відповідним текстом.
"""


class NameLenException(Exception):
    pass


class PasswordException(Exception):
    pass


def login_valid(username, password):
    correct_name = ''
    correct_pass = ''

    name_len = len(username)

    if name_len >= 3 and name_len <= 50:
        correct_name = 'username is OK'
    else:
        raise NameLenException(
            'Username is too short ot too long!'
        )

    pass_len = len(password)

    if pass_len >= 8 and any(x.isdigit() for x in password):
        correct_pass = 'password is OK'
    else:
        raise PasswordException(
            'Password must contain 8 or more '
            + 'characters and at least 1 digit.'
        )

    if any(x.isupper() for x in password):
        correct_pass = 'password is OK'
    else:
        raise PasswordException(
            'Password must contain at least 1 uppercase letter.'
        )

    correct_login = correct_name + '\n' + correct_pass
    print(correct_login)

    return correct_login


username = input('Enter username: ')
password = input('Enter password: ')

login_valid(username, password)
