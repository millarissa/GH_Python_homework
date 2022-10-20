"""
Написати функцію <prime_list>, яка прийматиме 2 аргументи -
початок і кінець діапазона, і вертатиме список простих чисел
всередині цього діапазона. Не забудьте про перевірку
на валідність введених даних та у випадку невідповідності -
виведіть повідомлення.
"""


def prime_list(start, stop):
    prime_list = []
    
    for num in range(start,stop):
        prime = True
        
        if num == 0 or num == 1:
            prime = False
        else:            
            for x in range(2, num):
                if(num % x == 0):
                    prime = False
            if prime:
                prime_list.append(num)
        
    print(prime_list)
    
    return prime_list


try:
    start = int(input('Enter start number: '))
    stop = int(input('Enter end number: '))

    prime_list(start, stop)
    
except ValueError:
    print('Wrong numbers. Please, check and try again.')
    
    start = int(input('Enter start number: '))
    stop = int(input('Enter end number: '))

    prime_list(start, stop)
