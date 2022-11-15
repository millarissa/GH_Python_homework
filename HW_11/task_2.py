"""
Створити клас Person, в якому буде присутнім метод __init__
який буде приймати якісь аргументи, які зберігатиме в відповідні змінні.

"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_name(self):
        print('Name is', self.name)

    def show_age(self):
        print('Age is', self.age)

    def show_all_information(self):
        print('User', self.name, 'is', self.age)


person_1 = Person('Jeff', 48)
person_2 = Person('Lisa', 24)
person_1.profession = 'Baker'
person_2.profession = 'Artist'

person_1.print_name()
person_1.show_age()
print(person_1.profession)

person_2.show_all_information()
print(person_2.profession)
