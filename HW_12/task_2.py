"""
Створіть за допомогою класів та продемонструйте свою реалізацію шкільної бібліотеки
"""

import sqlite3
import datetime
from sqlite3 import Error
from tabulate import tabulate


class DataBaseOperations:

    def create_connection(self, db_file):
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            return conn
        except Error as e:
            print(e)

        return conn

    def create_table(self, conn, create_table_sql):
        try:
            c = conn.cursor()
            c.execute(create_table_sql)
        except Error as e:
            print(e)

        return

    def create_users(self, conn):
        sql = """ CREATE TABLE IF NOT EXISTS users (
                                            name text,
                                            password text,
                                            role text,                                            
                                            UNIQUE(name, password)
                                        ); """

        self.create_table(conn, sql)

        return

    def create_books(self, conn):
        sql = """ CREATE TABLE IF NOT EXISTS books (
                                            name text,
                                            author text,
                                            category text,
                                            rating text,
                                            num_cupboard integer,
                                            num_shelf integer,
                                            status text,                                          
                                            UNIQUE(name)
                                        ); """

        self.create_table(conn, sql)

        return

    def update_users(self, conn, user):
        sql = ''' INSERT INTO users( 
                                    name, 
                                    password, 
                                    role
                                    )
                  VALUES(?,?,?)'''
        cur = conn.cursor()
        cur.execute(sql, user)
        conn.commit()

        return cur.lastrowid

    def update_book_status(self, conn, book_info):
        sql = ''' UPDATE books
                  SET status = ?
                  WHERE name = ?'''
        cur = conn.cursor()
        cur.execute(sql, book_info)
        conn.commit()

    def create_new_book(self, conn, book_data):
        sql = ''' INSERT INTO book(
                              book_name,
                              category,
                              reader_name,
                              start_date,
                              return_date,
                              reading_status
                            )
                  VALUES(?,?,?,?,?,?)'''
        cur = conn.cursor()
        cur.execute(sql, book_data)
        conn.commit()


class BookLogs:

    def create_book_logs(self, conn, booklogs):
        sql = """ CREATE TABLE IF NOT EXISTS booklogs (
                                            book_name text,
                                            category text,
                                            reader_name text,
                                            start_date date,
                                            return_date date,
                                            reading_status text
                                        ); """
        database.create_table(conn, sql)
        sql = ''' INSERT INTO booklogs(
                              book_name,
                              category,
                              reader_name,
                              start_date,
                              return_date,
                              reading_status
                            )
                  VALUES(?,?,?,?,?,?)'''
        cur = conn.cursor()
        cur.execute(sql, booklogs)
        conn.commit()

        return cur.lastrowid

    def update_logs_status(self, conn, log_info):
        sql = ''' UPDATE booklogs
                  SET reading_status = ?
                  WHERE book_name = ? AND reader_name = ?'''
        cur = conn.cursor()
        cur.execute(sql, log_info)
        conn.commit()


class MenuOptions:

    def start_menu(self, conn):
        menu_text = """
                 Welcome to library! Choose operation:
                 1: Login
                 2: Register
                 3: Exit
        """
        print(menu_text)
        operation_num = int(input('Enter operation number: '))
        if operation_num == 1:
            login.login_user(conn)
        elif operation_num == 2:
            login.register_user(conn)
        elif operation_num == 3:
            print('Goodbye!')
        else:
            print('Wrong operation number! Please, try again.')
        return

    def welcome_text(self, conn, name):
        if login.check_if_librarian(conn, name):
            menu_text = """
                Choose operation:
                1: Check all books in library
                2: Check books on hands
                3. Add new book
                4: Exit
            """
        else:
            menu_text = """
                 Choose operation:
                 1: Check all books in library
                 2: Take book
                 3: Return book
                 4: Check my taken books
                 5: Exit
            """

        print(menu_text)
        return

    def menu_reader(self, conn, operation_num, name):
        if operation_num == 1:
            reader.check_all_books(conn)
        elif operation_num == 2:
            reader.take_book(conn, name)
        elif operation_num == 3:
            reader.return_book(conn, name)
        elif operation_num == 4:
            reader.check_taken_books(conn, name)
        elif operation_num == 5:
            print('Goodbye!')
        else:
            print('Wrong operation number! Please, try again.')
        return

    def menu_librarian(self, conn, operation_num):
        if operation_num == 1:
            librarian.check_all_books(conn)
        elif operation_num == 2:
            librarian.check_taken_books(conn)
        elif operation_num == 3:
            librarian.add_book(conn)
        elif operation_num == 4:
            print('Goodbye!')
        else:
            print('Wrong operation number! Please, try again.')
        return


class LoginOperations:
    def login_user(self, conn):
        name = input('Enter your name: ')
        password = input('Enter your password: ')

        if self.check_password(conn, name, password):

            welkome_text = '_________WELCOME AS ' + name.upper() + '________'
            print(welkome_text)
            if self.check_if_librarian(conn, name):
                start.welcome_text(conn, name)
                operation_num = int(input('Enter operation number: '))
                start.menu_librarian(conn, operation_num)

                while operation_num != 5:
                    start.welcome_text(conn, name)
                    operation_num = int(input('Enter operation number: '))
                    start.menu_librarian(conn, operation_num)

            else:
                start.welcome_text(conn, name)
                operation_num = int(input('Enter operation number: '))
                start.menu_reader(conn, operation_num, name)

                while operation_num != 5:
                    start.welcome_text(conn, name)
                    operation_num = int(input('Enter operation number: '))
                    start.menu_reader(conn, operation_num, name)
        else:
            print('Wrond username or password.')

        return

    def check_password(self, conn, name, password):
        correct_login = False

        cur = conn.cursor()
        cur.execute("SELECT name, password FROM users")

        login = cur.fetchall()
        for user in login:
            if name == user[0] and password == user[1]:
                correct_login = True
                break

        return correct_login

    def check_if_librarian(self, conn, name):
        is_librarian = False

        cur = conn.cursor()
        cur.execute("SELECT name, role FROM users WHERE name=?", (name,))

        user_role = cur.fetchone()
        if user_role == 'librarian':
            is_librarian = True

        return is_librarian

    def register_user(self, conn):
        print_text = """
                Please, enter new user.
                Name must be between 3 and 50 characters long.
                Password must be longer than 8 characters,
                and contain at least 1 digit and 1 capital letter.
                Role can be 'student' or 'teacher'.
            """
        print(print_text)
        new_name = input('Enter your name: ')
        new_password = input('Enter your password: ')
        new_role = input('Enter your role: ')
        if self.check_new_user(new_name, new_password, new_role):
            user = (new_name, new_password, new_role)
            database.update_users(conn, user)
            print('User was successfully added.')
            start.start_menu(conn)
        else:
            print('Please, try again.')
        return

    def check_new_user(self, name, password, role):
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

        if role == 'student' or role == 'teacher':
            correct_role = True
        else:
            correct_role = False
            print('Please, enter correct role.')

        if correct_name and correct_pass and correct_role:
            correct_login = True

        return correct_login


class ReaderOperations:

    def check_all_books(self, conn):
        cur = conn.cursor()
        cur.execute(""" SELECT name, 
                               author, 
                               category,
                               rating, 
                               num_cupboard, 
                               num_shelf
                        FROM books
                        WHERE status=?""",
                    ('Free',)
                    )

        all_books = cur.fetchall()
        headers = [
            'Book name',
            'Author',
            'category',
            'Rating',
            'Board',
            'Shelf'
        ]
        print('List of all books in the library:')
        print(tabulate(all_books, headers, tablefmt="grid"))

        return all_books

    def check_taken_books(self, conn, name):
        cur = conn.cursor()
        cur.execute(""" SELECT book_name, category, start_date, return_date
                        FROM booklogs
                        WHERE reader_name = ? AND reading_status = ?""",
                    (name, 'Progress')
                    )

        reader_books = cur.fetchall()
        headers = [
            'Book name',
            'Start date',
            'Return to'
        ]
        print('List of my books:')
        print(tabulate(reader_books, headers, tablefmt="grid"))
        return

    def take_book(self, conn, name):
        book_name = input('Enter name of a book you want to take: ')

        cur = conn.cursor()
        cur.execute(""" SELECT rating, status
                        FROM books
                        WHERE name=?""",
                    (book_name,)
                    )
        book_info = cur.fetchone()
        book_rating = book_info[0]
        book_status = book_info[1]

        cur.execute(""" SELECT role
                        FROM users
                        WHERE name=?""",
                    (name,)
                    )
        reader_role = cur.fetchone()

        if reader_role[0] == 'student' and book_rating == 'NC':
            print('Sorry, you are too young for this book.')
        else:
            if book_status == 'Free':
                start_date = datetime.date.today()
                return_date = start_date + datetime.timedelta(days=10)
                reading_status = 'Progress'

                book_log = (book_name, name, start_date, return_date, reading_status)
                booklog.create_book_logs(conn, book_log)

                new_status = 'Taken'
                book_info = (new_status, book_name)
                database.update_book_status(conn, book_info)

                print('Ok, read it!')
            else:
                print('Sorry, someone is reading it.')

        return

    def return_book(self, conn, name):
        book_name = input('Enter name of a book you want to return: ')
        cur = conn.cursor()
        cur.execute(""" SELECT book_name
                        FROM booklogs
                        WHERE reader_name=?""",
                    (name,)
                    )
        book_info = cur.fetchone()

        if book_info[0]:
            reading_status = 'Finished'
            log_info = (reading_status, book_name, name)
            booklog.update_logs_status(conn, log_info)

            new_status = 'Free'
            book_info = (new_status, book_name)
            database.update_book_status(conn, book_info)
            print('Book is returned to library.')
        else:
            print('You haven`t this book.')
        return


class LibrarianOperations:
    def check_all_books(self, conn):
        cur = conn.cursor()
        cur.execute(""" SELECT name, 
                               author, 
                               category,
                               rating, 
                               num_cupboard, 
                               num_shelf,
                               status
                        FROM books"""
                    )

        all_books = cur.fetchall()
        headers = [
            'Book name',
            'Author',
            'category',
            'Rating',
            'Board',
            'Shelf',
            'Status'
        ]
        print('List of all books in the library:')
        print(tabulate(all_books, headers, tablefmt="grid"))

        return all_books

    def check_taken_books(self, conn):
        cur = conn.cursor()
        cur.execute(""" SELECT book_name, category, reader_name, start_date, return_date
                        FROM booklogs
                        WHERE reading_status = ?""",
                    ('Progress')
                    )

        taken_books = cur.fetchall()
        headers = [
            'Book name',
            'category',
            'Reader',
            'Start date',
            'Return to'
        ]
        print('List of taken books:')
        print(tabulate(taken_books, headers, tablefmt="grid"))
        return

    def add_book(self, conn):
        print('Enter info about new book.')
        book_name = input('Book name: ')
        book_author = input('Author name: ')
        category = input('Category name: ')
        rating = input('Rating (Choose one:G, R, NC): ')
        num_board = int(input('Cupboard number: '))
        num_shelf = int(input('Shelf number: '))
        status = 'Free'

        book_data = (
                     book_name,
                     book_author,
                     category,
                     rating,
                     num_board,
                     num_shelf,
                     status
                    )
        database.create_new_book(conn, book_data)
        print('Book added.')
        return
        

conn = sqlite3.connect('library.db')
database = DataBaseOperations()
start = MenuOptions()
login = LoginOperations()
reader = ReaderOperations()
booklog = BookLogs()
librarian = LibrarianOperations()

if __name__ == "__main__":
    if conn is not None:
        database.create_users(conn)
        database.create_books(conn)
    else:
        print("Error! Cannot create the database connection.")

    with conn:
        start.start_menu(conn)
