"""
На основі попередньої функції створити наступний скрипт:
   а) створити список із парами ім'я/пароль
   різноманітних видів (орієнтуйтесь по правилам своєї функції) -
   як валідні, так і ні;
   б) створити цикл, який пройдеться по цьому циклу і,
   користуючись валідатором, перевірить ці дані і надрукує
   для кожної пари значень відповідне повідомлення
"""


class NameLenException(Exception):
    pass


class PasswordException(Exception):
    pass


def login_valid(login_list):

    for username, password in login_list:
        correct_name = False
        correct_pass = False
        correct_login = ''

        print('Name:', username, '\n' + 'Password:', password)

        name_len = len(username)
        pass_len = len(password)

        if name_len >= 3 and name_len <= 50:
            correct_name = True
        else:
            try:
                raise NameLenException(
                    'Username is too short ot too long!'
                )
            except NameLenException as ex:
                correct_name = False
                print(ex)

        if pass_len >= 8 and any(x.isdigit() for x in password):
            correct_pass = True
        else:
            try:
                raise PasswordException(
                    'Password must contain 8 or more '
                    + 'characters and at least 1 digit.'
                )
            except PasswordException as ex:
                correct_pass = False
                print(ex)

        if any(x.isupper() for x in password):
            correct_pass = True
        else:
            try:
                raise PasswordException(
                    'Password must contain at least 1 uppercase letter.'
                )
            except PasswordException as ex:
                correct_pass = False
                print(ex)

        if correct_name and correct_pass:
            correct_login = 'User is OK' + '\n'

        print(correct_login)

    return correct_login


login_list = [
        ('rosatyler', 'RosaTyler12345'),
        ('marthajones', 'mj13'),
        ('dn', 'DonnaNoble1984'),
        ('klara', '1RunYouCleverBoyAndRemember1'),
        ('pond', 'Pond4Pond')
        ]

login_valid(login_list)
