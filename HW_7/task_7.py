"""
Напишіть функцію, яка приймає 2 списки.
Результатом має бути новий список, в якому знаходяться
елементи першого списку, яких немає в другому.
Порядок елементів, що залишилися має відповідати порядку
в першому (оригінальному) списку.
Реалізуйте обчислення за допомогою генератора в один рядок.
"""


def list_difference(list1, list2):

    set2 = set(list2)
    result = [x for x in list1 if x not in set2]

    print(result)

    return


list1 = list(input('Enter first list: '))
list2 = list(input('Enter second list: '))


list_difference(list1, list2)
