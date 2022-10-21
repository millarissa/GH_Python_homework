"""
Написати функцію <fibonacci>, яка приймає один аргумент
і виводить всі числа Фібоначчі, що не перевищують його.
"""

def fibonacci(num):
    fib_numbers = []
    res_list = []

    if num != 1:
        fib_numbers = [0, 1]
        
        for i in range(1, num - 1):
            fib_numbers.append(fib_numbers[i - 1] + fib_numbers[i])    
            res_list = [i for i in fib_numbers if i <= num]

    else:
        res_list = [0]
        
    print(res_list)
    
    return res_list

try:
    num = int(input('Enter number: '))
    fibonacci(num)

except ValueError:
    print('Wrong value, please, try again.')
