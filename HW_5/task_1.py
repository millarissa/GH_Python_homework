"""
Написати функцію <square>, яка прийматиме один аргумент -
сторону квадрата, і вертатиме 3 значення у вигляді кортежа:
периметр квадрата, площа квадрата та його діагональ.
"""

import math


def square(square_side):
    perimeter = 4 * square_side
    area = square_side ** 2
    diagonal = round(math.sqrt(2) * square_side, 2)
    
    square_tuple = (perimeter, area, diagonal)    
    print(square_tuple)
    
    return

try:
    square_side = int(input('Enter square side length: '))
    square(square_side)
    
except ValueError:
    print('Wrong value, please, try again')
