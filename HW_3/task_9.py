"""
Користувачем вводиться початковий і кінцевий рік.
Створити цикл, який виведе всі високосні роки в цьому проміжку
(границі включно).
P.S. Рік є високосним, якщо він кратний 4, але не кратний 100,
а також якщо він кратний 400.
"""

start_year = int(input('Enter start year: '))
end_year = int(input('Enter end year: '))

print('List of leap years between ', start_year, 'and', end_year, ':')
for year in range(start_year, end_year):
    if year % 400 == 0:
        print(year)
    elif year % 100 == 0:
        continue
    elif year % 4 == 0:
         print(year)
