"""
Створіть ф-цiю, яка буде отримувати довільні рядки
та яка обробляє наступні випадки:
-  якщо довжина рядка в діапазоні 30-50 (включно) ->
    прiнтує довжину рядка, кiлькiсть букв та цифр
-  якщо довжина менше 30 -> прiнтує суму всіх чисел
    та окремо рядок без цифр та знаків лише з буквами
    (без пробілів)
-  якщо довжина більше 50 -> прінтує окремо рядок лише з буквами капсом
    та рядок лише з цифрами та символами без пробілів. 
"""

def transform_line(user_line):
    line_len = len(user_line)
    if line_len < 30:
        num = sum(int(x) for x in user_line if x.isdigit())
        line_text = ''.join(x for x in user_line if x.isalpha())
        res = ('Сума цифр: ' + str(num) + '\n'
            'Новий рядок: ' + line_text 
        )
    elif line_len in range(30, 51):
        num = sum(x.isdigit() for x in user_line)
        lett = sum(x.isalpha() for x in user_line)
        res = ('Довжина рядка: ' + str(line_len) + '\n'
            'Всього букв: ' + str(lett) + '\n'
            'Всього цифр: ' + str(num)
        )
    if line_len > 50:
        line_symb = ''.join(
            x for x in user_line if not x.isalpha() and not x.isspace()
        )
        line_text = ''.join(x for x in user_line if x.isalpha())
        res = ('Рядок капсом: ' + line_text.upper() + '\n'
            'Рядок без букв: ' + line_symb 
        )
    print(res)
    return res

user_line = input('Enter random numbers, letters and symbols: ')
transform_line(user_line)
