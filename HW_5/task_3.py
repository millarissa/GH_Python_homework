"""
Написати функцию <is_prime>, яка прийматиме 1 аргумент -
число від 0 до 1000, и яка вертатиме True,
якщо це число просте і False - якщо ні.
"""

def is_prime(num):
    prime = False
    
    if num < 0 or num > 1000:
        prime = 'Number is out of range'
    else:
        if num == 0 or num == 1:
            prime = False
        else: 
            for x in range(2, num):
                if num % x == 0:
                    prime = False
                    break
                else:
                    prime = True
                    
    return prime

try:
    num = int(input('Enter number from 0 to 1000: ')) 
    print(is_prime(num))

except ValueError:
    print('Wrong value, please, try again.')
