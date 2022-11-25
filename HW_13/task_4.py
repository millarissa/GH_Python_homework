"""
Створіть клас, який буде повністю копіювати поведінку list,
за виключенням того, що індекси в ньому мають починатися з 1,
а індекс 0 має викидати помилку
(такого ж типу, яку кидає list якщо звернутися до неіснуючого індексу)
"""


class NewList(list):
    def __getitem__(self, index):
        if index == 0:
            raise ValueError
        if index > 0:
            index = index - 1
        return list.__getitem__(self, index)


new_list = NewList('12345')
print('list:', new_list)
print('[1] =', new_list[1])
print('[-1] =', new_list[-1])


