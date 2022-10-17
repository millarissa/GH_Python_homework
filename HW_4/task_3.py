"""
Користувач вводить змінні "x" та "y"
з довільними цифровими значеннями.
Створіть просту умовну конструкцію
(звiсно вона повинна бути в тiлi ф-цiї),
під час виконання якої буде перевірятися рівність
змінних "x" та "y" та у випадку нерівності -
виводити ще і різницю.
    Повинні працювати такі умови
    (x, y, z заміність на відповідні числа):
    x > y;       вiдповiдь - "х бiльше нiж у на z"
    x < y;       вiдповiдь - "у бiльше нiж х на z"
    x == y.      відповідь - "х дорівнює y"
"""

def get_difference(num_1, num_2):
    if num_1 > num_2:
        diff = num_1 - num_2
        result = str(num_1) + ' бiльше нiж ' + str(num_2) + ' на ' + str(diff)
    elif num_1 < num_2:
        diff = num_2 - num_1
        result = str(num_2) + ' бiльше нiж ' + str(num_1) + ' на ' + str(diff)
    else:
        result = str(num_1) + ' дорівнює ' + str(num_2)
    print(result)
    return result  

try:
    num_1 = int(input('Enter first number: '))
    num_2 = int(input('Enter second number: '))
    get_difference(num_1, num_2)34

except ValueError:
    print('Wrong value, enter number, please.')
