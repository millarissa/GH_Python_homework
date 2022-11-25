"""
Створіть клас Car, який буде мати властивість year (рік випуску).
Додайте всі необхідні методи до класу, щоб можна було виконувати
порівняння car1 > car2 , яке буде показувати, що car1 старша за car2.
Також, операція car1 - car2 повинна повернути різницю між роками випуску.
"""


class Car:
    def __init__(self, year):
        self.year = year

    def __gt__(self, other):
        res = ''
        if self.year < other.year:
            res = 'Car1 is older.'
        else:
            res = 'Car2 is older'
        return res

    def __sub__(self, other):
        age = abs(self.year - other.year)
        res = 'Age difference is: ' + str(age) + ' years.'
        return res


car1 = Car(2018)
car2 = Car(2016)
print(car1 > car2)
print(car1 - car2)
