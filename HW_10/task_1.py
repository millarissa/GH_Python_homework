"""
Банкомат
"""


import sqlite3
from sqlite3 import Error
from tabulate import tabulate


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

    return


def create_users(conn):
    sql = """ CREATE TABLE IF NOT EXISTS users (
                                        name text,
                                        password text,
                                        UNIQUE(name, password)
                                    ); """

    create_table(conn, sql)

    return


def insert_users(conn):
    users_list = (
        ('admin', 'admin'),
        ('rosatyler', 'RosaTyler12345'),
        ('donna', 'DonnaNoble1984'),
        ('klara', '1RunYouCleverBoyAndRemember1'),
        ('pond', 'Pond4Pond')
    )

    sql = ''' INSERT OR IGNORE INTO users(name, password)
              VALUES(?,?)'''
    cur = conn.cursor()

    for user in users_list:
        cur.execute(sql, user)

    conn.commit()

    return cur.lastrowid


def check_password(conn, name, password):
    correct_login = False

    cur = conn.cursor()
    cur.execute("SELECT name, password FROM users")

    login = cur.fetchall()
    for user in login:
        if name == user[0] or password == user[1]:
            correct_login = True
            break

    return correct_login


def check_new_user(name, password):
    correct_login = False

    name_len = len(name)

    if 3 <= name_len <= 50:
        correct_name = True
    else:
        correct_name = False
        print('Username is too short ot too long!')

    pass_len = len(password)

    if pass_len >= 8 and any(x.isdigit() for x in password):
        correct_pass = True

        if any(x.isupper() for x in password):
            correct_pass = True
        else:
            correct_pass = False
            print(
                'Password must contain at least 1 uppercase letter.'
                )
    else:
        correct_pass = False
        print(
            'Password must contain 8 or more '
            + 'characters and at least 1 digit.'
            )

    if correct_name and correct_pass:
        correct_login = True

    return correct_login


def update_users(conn, user):
    sql = ''' INSERT INTO users(name,password)
              VALUES(?,?)'''
    cur = conn.cursor()
    cur.execute(sql, user)
    conn.commit()

    return cur.lastrowid


def create_balance(conn):
    sql = """ CREATE TABLE IF NOT EXISTS balance (
                                        name text,
                                        balance integer,
                                        UNIQUE(name)
                                    ); """

    create_table(conn, sql)
    sql = ''' INSERT OR IGNORE INTO balance(name, balance)
              VALUES(?,?)'''
    cur = conn.cursor()

    balance = ('admin', '140000')
    cur.execute(sql, balance)
    conn.commit()

    return cur.lastrowid


def create_banknotes(conn):
    sql = """ CREATE TABLE IF NOT EXISTS banknotes (
                                        denomination text,
                                        amount integer,
                                        UNIQUE(denomination)
                                    ); """

    create_table(conn, sql)
    sql = ''' INSERT OR IGNORE INTO banknotes(denomination, amount)
              VALUES(?,?)'''
    cur = conn.cursor()

    banknotes = (
        ('10', '30000'),
        ('20', '10000'),
        ('50', '20000'),
        ('100', '20000'),
        ('200', '20000'),
        ('500', '10000'),
        ('1000', '30000')
        )

    for i in banknotes:
        cur.execute(sql, i)

    conn.commit()

    return cur.lastrowid


def create_user_balance(conn, name):
    sql = ''' INSERT OR IGNORE INTO balance(name, balance)
              VALUES(?,?)'''
    cur = conn.cursor()

    balance = (name, '0')
    cur.execute(sql, balance)
    conn.commit()

    return cur.lastrowid


def check_balance(conn, name):
    cur = conn.cursor()
    cur.execute("SELECT balance FROM balance WHERE name=?", (name,))

    balance = cur.fetchone()
    print('Your balance =', balance[0])
    return balance


def update_balance(conn, balance):
    sql = ''' UPDATE balance
              SET balance = ?
              WHERE name = ?'''
    cur = conn.cursor()
    cur.execute(sql, balance)
    conn.commit()
    return


def create_transactions(conn, transaction):
    sql = """ CREATE TABLE IF NOT EXISTS transactions (
                                        name text,
                                        operation text,
                                        old_balance integer,
                                        update_sum integer,
                                        new_balance integer
                                    ); """
    create_table(conn, sql)
    sql = ''' INSERT INTO transactions(
                          name,
                          operation,
                          old_balance,
                          update_sum,
                          new_balance
                        )
              VALUES(?,?,?,?,?)'''
    cur = conn.cursor()
    cur.execute(sql, transaction)
    conn.commit()
    return cur.lastrowid


def create_admin_transactions(conn, admin_transaction):
    sql = """ CREATE TABLE IF NOT EXISTS admin_transactions (
                                        denomination text,
                                        old_amount integer,
                                        new_amount integer,
                                        balance integer
                                    ); """
    create_table(conn, sql)
    sql = ''' INSERT INTO admin_transactions(
                              denomination,
                              old_amount,
                              new_amount,
                              balance
                          )
              VALUES(?,?,?,?)'''
    cur = conn.cursor()
    cur.execute(sql, admin_transaction)
    conn.commit()

    return cur.lastrowid


def update_banknotes_balance(conn, denomination, new_amount):
    cur = conn.cursor()

    sql_update = ''' UPDATE banknotes
                     SET amount = ?
                     WHERE denomination = ?'''
    cur.execute(sql_update, (new_amount, denomination))

    cur.execute("SELECT amount FROM banknotes")
    numbers = cur.fetchall()

    total_sum = 0

    for num in numbers:
        total_sum += num[0]

        sql_update_sum = ''' UPDATE balance
                             SET balance = ?
                             WHERE name = ?'''
        cur.execute(sql_update_sum, (total_sum, 'admin'))
        conn.commit()

    return


def withdraw_banknotes(conn, name, operation, available_banknotes, update_sum):
    cur = conn.cursor()
    available_banknotes.reverse()
    count_banknotes = len(available_banknotes)
    result_list = {'0': 0}
    result_cash = {}

    for i in range(0, count_banknotes + 1):
        banknote_in_list = int(available_banknotes[i])
        sub_list = {}

        for banknotes_sum, banknote in result_list.items():
            sub_sum = int(banknotes_sum) + banknote_in_list

            if sub_sum > update_sum:
                continue

            if sub_sum not in result_list:
                sub_list[sub_sum] = banknote_in_list

        result_list.update(sub_list)

        if update_sum in result_list:
            break

    if result_list[update_sum]:
        used_banknotes = []
        remained_sum = update_sum

        while remained_sum > 0:
            used_banknotes.append(result_list[remained_sum])
            remained_sum = remained_sum - result_list[remained_sum]

        for i in used_banknotes:
            result_cash[i] = used_banknotes.count(i)

        cur.execute(
                    "SELECT balance FROM balance WHERE name=?",
                    (name,)
                    )
        old_bal = cur.fetchone()
        old_bal = old_bal[0]
        new_bal = old_bal - update_sum

        print('Take your cash: ')

        for banknote, count in result_cash.items():
            cur.execute(
                "SELECT amount FROM banknotes WHERE denomination = ?",
                (banknote,)
            )
            old_amount = cur.fetchone()
            old_amount = old_amount[0]
            new_amount = old_amount - count

            update_banknotes_balance(conn, banknote, new_amount)
            print(count, 'x', banknote)

        update_balance(conn, (new_bal, name))
        transaction = (
                        name,
                        operation,
                        old_bal,
                        update_sum,
                        new_bal
                    )
        create_transactions(conn, transaction)
        print('Cash was succesfully withdrawed.')

    else:
        print('Sorry, there is no cash suitable to your sum.')

    return used_banknotes


def add_balanse(conn, name):
    try:
        operation = 'Adding'
        update_sum = int(input('Enter sum for adding to your balance: '))

        if update_sum > 0:
            change = update_sum % 10
            if change == 0:
                cur = conn.cursor()
                cur.execute(
                    "SELECT balance FROM balance WHERE name=?",
                    (name,)
                )
                old_bal = cur.fetchone()
                old_bal = old_bal[0]
                new_bal = old_bal + update_sum
                update_balance(conn, (new_bal, name))

                print('New sum sucsessfully added to your account.')

                transaction = (name, operation, old_bal, update_sum, new_bal)
                create_transactions(conn, transaction)
            else:
                update_sum = update_sum - change
                print('You can add sum only multiple to 10. '
                      + 'Change will be returned to you.'
                      )
                cur = conn.cursor()
                cur.execute(
                    "SELECT balance FROM balance WHERE name=?",
                    (name,)
                )
                old_bal = cur.fetchone()
                old_bal = old_bal[0]
                new_bal = old_bal + update_sum
                update_balance(conn, (new_bal, name))

                print('New sum (',
                      + update_sum,
                      + ') sucsessfully added to your account.'
                      )
                print('Change left:', change)

                transaction = (name, operation, old_bal, update_sum, new_bal)
                create_transactions(conn, transaction)

        else:
            print('You cannot add negative sum.')

    except ValueError:
        print('Sum must be entered in numbers.')

    return


def withdraw_balance(conn, name):
    try:
        cur = conn.cursor()
        operation = 'Withdraw'
        cur.execute('''SELECT denomination,
                              amount
                       FROM banknotes
                       WHERE amount > ?
                    ''',
                    (0,)
                    )
        den_available = cur.fetchall()
        available_list = []
        available_amount = []
        available_banknotes = []

        for den in den_available:
            available_list.append(den[0])
            available_amount.append(den[1])
            available_banknotes += [*[den[0]] * den[1]]

        print('Available banknotes are:', ', '.join(available_list), 'UAH')

        update_sum = int(input('Enter sum for withdraw from your balance: '))

        if update_sum > 0:
            cur.execute(
                    "SELECT balance FROM balance WHERE name=?",
                    (name,)
                )
            old_bal = cur.fetchone()
            old_bal = old_bal[0]

            cur.execute(
                    "SELECT balance FROM balance WHERE name=?",
                    ('admin',)
                )
            total_sum = cur.fetchone()
            if old_bal > update_sum:
                if total_sum[0] > update_sum:
                    change = update_sum % 10
                    if change == 0:
                        withdraw_banknotes(
                                            conn,
                                            name,
                                            operation,
                                            available_banknotes,
                                            update_sum
                                            )
                    else:
                        print('You can withdraw sum only multiple to 10.')
                else:
                    print('Not enough money in bancomat.')
            else:
                print('Not enough money on the account.')

        else:
            print('You cannot add negative sum.')

    except ValueError:
        print('Sum must be entered in numbers.')

    return


def check_bankomat_balance(conn):
    cur = conn.cursor()
    cur.execute("SELECT balance FROM balance WHERE name=?", ('admin',))

    balance = cur.fetchone()
    print('Bancomat balance =', balance[0])

    return balance


def check_banknotes(conn):
    cur = conn.cursor()
    cur.execute("SELECT denomination, amount FROM banknotes")

    numbers = cur.fetchall()
    headers = [
                'Banknote',
                'Amount'
              ]
    print('Your operations:')
    print(tabulate(numbers, headers, tablefmt="grid"))
    return numbers


def change_banknotes(conn):
    banknote = input('Enter banknote denomination: ')

    banknotes_list = []
    cur = conn.cursor()
    cur.execute("SELECT denomination FROM banknotes")
    sql_select = cur.fetchall()

    for list_elem in sql_select:
        banknotes_list.append(list_elem[0])

    if banknote in banknotes_list:
        new_amount = int(input('Enter new banknote amount: '))

        if new_amount >= 0:

            cur.execute(
                    "SELECT amount FROM banknotes WHERE denomination = ?",
                    (banknote,)
            )
            old_amount = cur.fetchone()
            old_amount = old_amount[0]

            sql_update = ''' UPDATE banknotes
                             SET amount = ?
                             WHERE denomination = ?'''
            cur.execute(sql_update, (new_amount, banknote))
            print('Amount of banknotes was sucsessfully changed.')

            cur.execute("SELECT amount FROM banknotes")
            numbers = cur.fetchall()

            total_sum = 0

            for num in numbers:
                total_sum += num[0]

            sql_update_sum = ''' UPDATE balance
                                 SET balance = ?
                                 WHERE name = ?'''
            cur.execute(sql_update_sum, (total_sum, 'admin'))
            conn.commit()

            admin_transaction = (
                        banknote,
                        old_amount,
                        new_amount,
                        total_sum
                    )
            create_admin_transactions(conn, admin_transaction)
            print('Bancomat balance was sucsessfully changed.')

        else:
            print('You cannot use negative amount.')

    else:
        print('Wrong denomination.')

    return


def login_user(conn):
    name = input('Enter your name: ')
    password = input('Enter your password: ')

    if check_password(conn, name, password):
        create_user_balance(conn, name)

        welkome_text = '___________WELCOME AS ' + name.upper() + '___________'
        print(welkome_text)
        if name == 'admin':
            welcome_text(conn, name)
            operation_num = int(input('Enter operation number: '))
            menu_admin(conn, operation_num)

            while operation_num != 5:
                welcome_text(conn, name)
                operation_num = int(input('Enter operation number: '))
                menu_admin(conn, operation_num)

        else:
            welcome_text(conn, name)
            operation_num = int(input('Enter operation number: '))
            menu(conn, operation_num, name)

            while operation_num != 5:
                welcome_text(conn, name)
                operation_num = int(input('Enter operation number: '))
                menu(conn, operation_num, name)
    else:
        print('Wrond username or password.')

    return


def register_user(conn):
    print_text = """
            Please, enter new user.
            Name must be between 3 and 50 characters long.
            Password must be longer than 8 characters,
            and contain at least 1 digit and 1 capital letter.
        """
    print(print_text)
    new_name = input('Enter your name: ')
    new_password = input('Enter your password: ')
    if check_new_user(new_name, new_password):
        user = (new_name, new_password)
        update_users(conn, user)
        print('User was successfully added.')
        start_menu(conn)
    else:
        print('Please, try again.')
    return


def transactions_history(conn, name):
    cur = conn.cursor()
    cur.execute(""" SELECT operation,
                           old_balance,
                           update_sum,
                           new_balance
                    FROM transactions
                    WHERE name=?""",
                (name,)
                )

    sql_select = cur.fetchall()
    headers = [
                'Operation',
                'Balance',
                'Update sum',
                'New balance'
              ]
    print('Your operations:')
    print(tabulate(sql_select, headers, tablefmt="grid"))

    return sql_select


def transactions_history_admin(conn):
    choose_text = """
            Choose operation:
            1: Check users transactions
            2: Check admin transactions
            3: Exit
        """
    print(choose_text)
    operation_num = int(input('Enter operation number: '))

    cur = conn.cursor()

    if operation_num == 1:
        cur.execute(""" SELECT name,
                               operation,
                               old_balance,
                               update_sum,
                               new_balance
                        FROM transactions"""
                    )

        sql_select = cur.fetchall()
        headers = [
                    'User Name',
                    'Operation',
                    'Balance',
                    'Update sum',
                    'New balance'
        ]
        print('Users operations:')
        print(tabulate(sql_select, headers, tablefmt="grid"))

    elif operation_num == 2:
        cur.execute(""" SELECT denomination,
                               old_amount,
                               new_amount,
                               balance
                        FROM admin_transactions"""
                    )

        sql_select = cur.fetchall()
        headers = [
                    'Banknotes',
                    'Old amount',
                    'New amount',
                    'Balance'
        ]
        print('Admin operations:')
        print(tabulate(sql_select, headers, tablefmt="grid"))

    elif operation_num == 3:
        print('Returning to admin menu.')
        welcome_text(conn, 'admin')
        operation_num = int(input('Enter operation number: '))
        menu_admin(conn, operation_num)

    else:
        print('Wrong operation number! Please, try again.')

    return


def transfer_money(conn, name):
    cur = conn.cursor()
    operation = 'Transfer Send'
    address_name = input('Enter name of another account to transfer:')
    update_sum = int(input('Enter sum to transfer: '))

    if update_sum > 0:
        cur.execute("SELECT balance FROM balance WHERE name=?", (name,))
        old_bal = cur.fetchone()
        old_bal = old_bal[0]

        if old_bal > update_sum:
            new_bal = old_bal - update_sum
            update_balance(conn, (new_bal, name))
            transaction = (
                            name,
                            operation,
                            old_bal,
                            update_sum,
                            new_bal
                            )
            create_transactions(conn, transaction)

        else:
            print('Not enough money on the account.')

    else:
        print('You cannot send negative sum.')

    address_operation = 'Transfer Recieve'
    cur = conn.cursor()
    cur.execute("SELECT balance FROM balance WHERE name=?", (address_name,))
    address_old_bal = cur.fetchone()

    if address_old_bal is None:
        create_user_balance(conn, address_name)

    cur.execute("SELECT balance FROM balance WHERE name=?", (address_name,))
    address_old_bal = cur.fetchone()
    address_old_bal = address_old_bal[0]

    address_new_bal = address_old_bal + update_sum
    update_balance(conn, (address_new_bal, address_name))
    transaction = (
                    address_name,
                    address_operation,
                    address_old_bal,
                    update_sum,
                    address_new_bal
                    )
    create_transactions(conn, transaction)
    print('Sucessful transaction.')

    return


def start_menu(conn):
    menu_text = """
             Hello! Choose operation:
             1: Login
             2: Register
             3: Exit
    """
    print(menu_text)
    operation_num = int(input('Enter operation number: '))

    if operation_num == 1:
        login_user(conn)
    elif operation_num == 2:
        register_user(conn)
    elif operation_num == 3:
        print('Goodbye!')
    else:
        print('Wrong operation number! Please, try again.')
    return


def menu(conn, operation_num, name):
    if operation_num == 1:
        check_balance(conn, name)
    elif operation_num == 2:
        add_balanse(conn, name)
    elif operation_num == 3:
        withdraw_balance(conn, name)
    elif operation_num == 4:
        transfer_money(conn, name)
    elif operation_num == 5:
        transactions_history(conn, name)
    elif operation_num == 6:
        print('Goodbye,', name)
        start_menu(conn)
    else:
        print('Wrong operation number! Please, try again.')

    return


def menu_admin(conn, operation_num):
    if operation_num == 1:
        check_bankomat_balance(conn)
    elif operation_num == 2:
        check_banknotes(conn)
    elif operation_num == 3:
        change_banknotes(conn)
    elif operation_num == 4:
        transactions_history_admin(conn)
    elif operation_num == 5:
        print('Goodbye, admin')
        start_menu(conn)
    else:
        print('Wrong operation number! Please, try again.')

    return


def welcome_text(conn, name):
    if name == 'admin':
        menu_text = """
            Choose operation:
            1: Check bankomat balance
            2: Check number of banknotes
            3: Change number of banknotes
            4: Operations history
            5: Exit
        """
    else:
        menu_text = """
             Choose operation:
             1: Check balance
             2: Add cash
             3: Withdraw cash
             4: Transfer money to another account
             5: Operations history
             6: Exit
        """

    print(menu_text)
    return


def start():
    conn = sqlite3.connect('bancomat.db')

    if conn is not None:
        create_users(conn)
        create_balance(conn)
        create_banknotes(conn)
    else:
        print("Error! Cannot create the database connection.")

    with conn:
        insert_users(conn)
        start_menu(conn)
    return


start()
