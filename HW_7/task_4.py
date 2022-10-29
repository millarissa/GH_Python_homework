"""
Реалізуйте генератор, який приймає на вхід будь-яку
ітерабельну послідовність (рядок, список, кортеж)
і повертає генератор, який буде повертати значення з
цієї послідовності, при цьому, якщо було повернено
останній елемент із послідовності - ітерація починається знову.
"""


def custom_generator(iterable):

    while 1:
        for j in iterable:
            yield j


for elem in custom_generator((1, 2, 3)):
    print(elem)