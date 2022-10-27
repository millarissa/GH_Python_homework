"""
Напишіть функцію,яка приймає рядок з декількох слів і
повертає довжину найкоротшого слова.
Реалізуйте обчислення за допомогою генератора в один рядок.
"""


def short_word(line):

    words = line.split()
    min_len = len(min(words, key=len))

    result = {len(x) for x in words if len(x) == min_len}
    print(result)

    return result


line = input('Enter string with several words: ')
short_word(line)
