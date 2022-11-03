"""
Банкомат
"""


import csv
from csv import reader
import json
import os


def create_login_file():
    fieldnames = ['name', 'password']
    login_list = [
        {'name': 'rosatyler',
            'password': 'RosaTyler12345'},
        {'name': 'donna',
            'password': 'DonnaNoble1984'},
        {'name': 'klara',
            'password': '1RunYouCleverBoyAndRemember1'},
        {'name': 'pond',
            'password': 'Pond4Pond'}
        ]
    with open('users_login.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(login_list)

    return


def create_balance_files(name):

    if not os.path.isfile(name+'_balance.txt'):
        with open(name+'_balance.txt', 'w') as f:
            f.write('0')

    return


def check_password(name, password):
    correct_login = False

    with open('users_login.csv', 'r') as read_file:
        csv_reader = reader(read_file)
        header = next(csv_reader)
        if header is not None:
            for row in csv_reader:
                if name == row[0] or password == row[1]:
                    correct_login = True
                    break

    return correct_login


def transactions(name, operation, old_bal, change_sum, new_bal):
    dictionary = {
        "operation_type": operation,
        "balance": old_bal,
        "change": change_sum,
        "final_balance": new_bal
    }

    if os.path.isfile('./'+name+'_transactions.json'):
        with open(name+'_transactions.json', 'a') as f:
            json.dump(dictionary, f)
    else:
        with open(name+'_transactions.json', 'w') as f:
            json.dump(dictionary, f)

    return


def check_balance(name):
    print(name, 'balance: ')

    with open(name+'_balance.txt', 'r') as f:
        print(f.read())

    return


def add_balance(name):
    try:
        operation = 'Adding'
        change_sum = int(input('Enter sum for adding to your balance: '))

        if change_sum > 0:

            with open(name+'_balance.txt', 'r') as f:
                old_bal = int(f.read())

            with open(name+'_balance.txt', 'w') as f:
                new_bal = old_bal + change_sum
                f.write(str(new_bal))
                print('New sum sucsessfully added to your account.')

            transactions(name, operation, old_bal, change_sum, new_bal)
        else:
            print('You cannot add negative sum.')

    except ValueError:
        print('Sum must be entered in numbers.')

    return


def withdraw_balance(name):
    try:
        operation = 'Withdraw'
        change_sum = int(input('Enter sum for withdraw from your balance: '))

        with open(name+'_balance.txt', 'r') as f:
            old_bal = int(f.read())

        if change_sum < old_bal:
            with open(name+'_balance.txt', 'w') as f:
                new_bal = old_bal - change_sum
                f.write(str(new_bal))
                print('Cash was sucsessfully withdrawed.')

            transactions(name, operation, old_bal, change_sum, new_bal)

        else:
            print('The amount is more than what you have in your account.')

    except ValueError:
        print('Sum must be entered in numbers.')

    return

def menu(operation_num, name):
    if operation_num == 1:
        check_balance(name)
    elif operation_num == 2:
        add_balance(name)
    elif operation_num == 3:
        withdraw_balance(name)
    elif operation_num == 4:
        print('Goodbye,', name)
    else:
        print('Wrong operation number! Please, try again.')
        
    return


def start():
    if not os.path.isfile('users_login.csv'):
        create_login_file()

    name = input('Enter your name: ')
    password = input('Enter your password: ')

    create_balance_files(name)

    if check_password(name, password):
        welcome_text = """
            WELCOME!
            Choose operation:
            1: Check balance
            2: Add cash
            3: Withdraw cash
            4: Exit
        """

        print(welcome_text)
        operation_num = int(input('Enter operation number: '))

        menu(operation_num, name)

        while operation_num != 4:
            welcome_text = """
                Choose operation:
                1: Check balance
                2: Add cash
                3: Withdraw cash
                4: Exit
            """

            print(welcome_text)
            operation_num = int(input('Enter operation number: '))
            menu(operation_num, name)

    else:
        print('Wrond username or password.')

    return


start()
