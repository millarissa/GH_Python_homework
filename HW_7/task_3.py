"""
Напишіть свою реалізацію функції range.
"""


def custom_range(one, two=None, three=None):

    if two is None:
        start = 0
        stop = one
        step = 1

    elif three is None:
        start = one
        stop = two
        step = 1

    else:
        if three == 0:
            raise ValueError('arg 3 must not be zero.')
        start = one
        stop = two
        step = three

    i = start

    if stop < 0 and step > 0:
        i = []

    elif stop > 0 and step < 0:
        i = []

    elif stop < 0 and step < 0:

        while i > stop:
            yield i
            i += step

    elif stop > 0 and step > 0:

        while i < stop:
            yield i
            i += step

    elif stop < start:
        i = []


for i in custom_range(1, 10, 2):
    print(i)
