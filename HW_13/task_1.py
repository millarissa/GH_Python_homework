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
        if self.year < other.year:
            res = True
        else:
            res = False
        return res

    def __sub__(self, other):
        age = abs(self.year - other.year)
        res = 'Age difference is: ' + str(age) + ' years.'
        return res


car1 = Car(2016)
car2 = Car(2019)
print(car1 > car2)
print(car1 - car2)
