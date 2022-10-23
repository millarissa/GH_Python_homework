"""
Створіть функцію, всередині якої будуть записано СПИСОК
із п'яти користувачів (ім'я та пароль).
Функція повинна приймати три аргументи: два -
обов'язкових (<username> та <password>) і третій -
необов'язковий параметр <silent>
(значення за замовчуванням - <False>).

Логіка наступна:
    якщо введено правильну пару ім'я/пароль - вертається True;
    якщо введено неправильну пару ім'я/пароль:
        якщо silent == True - функція повертає False
        якщо silent == False - породжується виключення LoginException
"""


class LoginException(Exception):
    pass


def login(username, password, silent=False):
    login_list = [
        ('user1', 'pass1'),
        ('user2', 'pass2'),
        ('user3', 'pass3'),
        ('user4', 'pass4'),
        ('user5', 'pass5')
        ]
    correct_login = False

    user_list = []
    pass_list = []

    for user in login_list:
        user_list.append(user[0])

    for passw in login_list:
        pass_list.append(passw[1])

    if username in user_list and password in pass_list:
        correct_login = True
    else:
        if silent:
            correct_login = False
        else:
            raise LoginException('Wrong username or password!')

    print(correct_login)

    return correct_login


username = input('Enter username: ')
password = input('Enter password: ')
silent = bool(input('Is silent? Enter True or False: ') or False)

login(username, password)
