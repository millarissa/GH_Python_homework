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
            ligth_list = list(itertools.repeat(ligth_col, 4))
            for ligth in ligth_list:
                yield ligth

        i += 1


def start():

    traffic_ligth = ['Red', 'Red', 'Yellow', 'Green']
    people_ligth = traffic_ligth.copy()
    traffic_ligth.reverse()

    x1 = 'People'
    x2 = 'Cars'
    print('{}\t{}'.format(x1, x2))
    print('______________')

    people_traffic = traffic_generator(people_ligth)
    cars_traffic = traffic_generator(traffic_ligth)

    for i, j in zip(people_traffic, cars_traffic):
        print('{}\t{}'.format(i, j))
        time.sleep(1)

    return


start()
