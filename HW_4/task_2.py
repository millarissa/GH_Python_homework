"""
Створіть 3 рiзних функцiї (на ваш вибiр).
Кожна з цих функцiй повинна повертати якийсь результат
(напр. інпут від юзера, результат математичної операції тощо).
Також створiть четверту ф-цiю, яка всередині
викликає 3 попередні, обробляє їх результат та
також повертає результат своєї роботи.
Таким чином ми будемо викликати одну (четверту) функцiю,
а вона в своєму тiлi - ще 3.
"""

def func_1():
    user_value = input('Enter some text: ')
    return user_value

def func_2(num_1, num_2):
    result = num_1**num_2
    return result

def func_3(num_1, num_2):
    result = num_1 + num_2
    return result

def func_4():
    try:
        num_1 = int(input('Enter first number: '))
        num_2 = int(input('Enter second number: '))

        print('User`s text: ', func_1())
        print(num_1, '**', num_2, '=', func_2(num_1, num_2))
        print(num_1, '+', num_2, '=', func_3(num_1, num_2))
    except ValueError:
        print('Wrong value, enter number, please.') 

func_4()
