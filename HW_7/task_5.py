"""
Напишіть функцію,яка приймає на вхід рядок та
повертає кількість окремих регістро-незалежних букв
та цифр, які зустрічаються в рядку більше ніж 1 раз.
Рядок буде складатися лише з цифр та букв (великих і малих).
Реалізуйте обчислення за допомогою генератора в один рядок
"""


def count_symbols(line):

    res_dict = {str(x): line.count(x) for x in line if line.count(x) > 1}
    print(res_dict)

    return res_dict


line = list(input('Enter line with letters and numbers: '))
count_symbols(line)
