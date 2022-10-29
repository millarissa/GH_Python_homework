"""
Напишіть свою реалізацію функції range.
"""


def custom_range(start, stop=None, step=None):

    if stop is None:
        stop = start
        start = 0
        step = 1

    elif step is None:
        step = 1

    else:
        if step == 0:
            raise ValueError('arg 3 must not be zero.')

    i = start

    if stop < 0 and step > 0:
        i = []

    elif step < 0:

        while i > stop:
            yield i
            i += step

    elif step > 0:

        while i < stop:
            yield i
            i += step

    elif stop < start:
        i = []


for i in custom_range(10, 2, -1):
    print(i)

