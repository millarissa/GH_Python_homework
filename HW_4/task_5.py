"""
Калькулятор. 
Повинна бути 1 функцiя, яка приймає 3 аргументи -
один з яких операцiя, яку зробити!
Аргументи брати від юзера (можна по одному -
окремо 2, окремо +, окремо 2; можна всі разом - типу 2 + 2).
Операції що мають бути присутні: +, -, *, /, %, //, **.
"""

def calculator(num_1, operation, num_2):
    if operation == '+':
        res = num_1 + num_2
    elif operation == '-':
        res = num_1 - num_2
    elif operation == '*':
        res = num_1 * num_2
    elif operation == '/':
        res = num_1 / num_2
    elif operation == '%':
        res = num_1 % num_2        
    elif operation == '//':
        res = num_1 // num_2              
    elif operation == '**':
        res = num_1 ** num_2
    else:
        print('Wrong operation symbol')

    print('{} {} {} = '.format(num_1, operation, num_2))
    print(res)
    return res

try:
    num_1 = int(input('Enter first number: '))
    operation = input('Enter operation (+, -, *, /, %, //, **): ')
    num_2 = int(input('Enter second number: '))

    calculator(num_1, operation, num_2)
except ValueError:
    print('Wrong value, check and enter again.')
    
    num_1 = int(input('Enter first number: '))
    operation = input('Enter operation (+, -, *, /, %, //, **): ')
    num_2 = int(input('Enter second number: '))

    calculator(num_1, operation, num_2)
