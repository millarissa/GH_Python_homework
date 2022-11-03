"""
Створити програму-емулятор світлофора для авто і пішоходів.
Після запуска програми на екран виводиться в лівій половині -
колір автомобільного, а в правій - пішохідного світлофора.
Кожну 1 секунду виводиться поточні кольори.
Через декілька ітерацій - відбувається зміна кольорів -
логіка така сама як і в звичайних світлофорах
(пішоходам зелений тільки коли автомобілям червоний).
"""


import time
import itertools


def traffic_generator(traffic_ligth):
    i = 1
    while i < 100:

        for ligth_col in traffic_ligth:
            if ligth_col == 'Yellow':
                count = 2
            else:
                count = 4
            ligth_list = list(itertools.repeat(ligth_col, count))
            for ligth in ligth_list:
                yield ligth

        i += 1


def start():

    car_traffic_ligth = ['Red', 'Yellow', 'Green', 'Yellow']
    people_traffic_ligth = ['Green', 'Red', 'Red']

    x1 = 'Cars'
    x2 = 'People'
    print('{}\t{}'.format(x1, x2))
    print('______________')

    people_traffic = traffic_generator(people_traffic_ligth)
    cars_traffic = traffic_generator(car_traffic_ligth)

    for i, j in zip(cars_traffic, people_traffic):
        print('{}\t{}'.format(i, j))
        time.sleep(1)

    return


start()

