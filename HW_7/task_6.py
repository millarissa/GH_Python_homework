"""
Напишіть функцію,яка приймає рядок з декількох слів і
повертає довжину найкоротшого слова.
Реалізуйте обчислення за допомогою генератора в один рядок.
"""


def short_word(line):

    words_len = {len(x) for x in line.split()}
    result = min(words_len)

    print(result)

    return result


line = input('Enter string with several words: ')
short_word(line)
