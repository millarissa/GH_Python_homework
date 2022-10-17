"""
Написати функцiю season, яка приймає один аргумент
(номер мiсяця вiд 1 до 12) та яка буде повертати пору року,
до якої цей мiсяць належить (зима, весна, лiто або осiнь).
У випадку некоректного введеного значення -
виводити відповідне повідомлення.
"""

def month_number(month_num):
    if (month_num in range(1,3)) or (month_num == 12):
        print('Winter')
    elif month_num in range(3,6):
        print('Spring')
    elif month_num in range(6,9):
        print('Summer')
    elif month_num in range(9,12):
        print('Autumn')
    else:
        print('Year has 12 months.')
  
try:
    month_num = int(input('Enter month number from 1 to 12: '))
    month_number(month_num)
except ValueError:
    print('Wrong value, enter number, please.') 
