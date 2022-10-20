"""
Написати функцію, яка буде реалізувати логіку
циклічного зсуву елементів в списку.
Тобто функція приймає два аргументи:
список і величину зсуву (якщо ця величина додатна -
пересуваємо з кінця на початок, якщо від'ємна -
навпаки - пересуваємо елементи з початку списку
в його кінець).
"""

from collections import deque


def slide_elements(user_list, slide):
    slide_object = deque(user_list)
    slide_object.rotate(slide)
    slide_list = list(slide_object)
    
    print(slide_list)

    return slide_list


try:
    user_list = input('Enter list of numbers, letters or symbols: ')
    slide = int(input('Enter slide value: '))

    slide_elements(user_list, slide)
    
except ValueError:
    print('Wrong value. Check and try again.')
    
    user_list = input('Enter list of numbers, letters or symbols: ')
    slide = int(input('Enter slide value: '))

    slide_elements(user_list, slide)
