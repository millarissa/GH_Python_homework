"""
Написати функцію, яка приймає два параметри:
ім'я (шлях) файлу та кількість символів.
Файл також додайте в репозиторій.
На екран має бути виведений список із трьома блоками -
символи з початку, із середини та з кінця файлу.
Кількість символів в блоках - та, яка введена в другому параметрі.
"""


def symbols(file, symbols_num):
    try:
        with open(file, "rb") as f:
            first_symbols = f.read(symbols_num).decode('utf-8')

            f.seek(0)
            data = f.read().decode('utf-8')

            if len(data) == 2 and symbols_num == 1:
                mid_symbols = '-'
            elif symbols_num % 2 == 0:
                middle = len(data) // 2 - 2
                f.seek(middle, 0)
                mid_symbols = f.read(symbols_num).decode('utf-8')
            else:
                print(len(data) // 2)
                middle = len(data) // 2 - 1
                f.seek(middle, 0)
                mid_symbols = f.read(symbols_num).decode('utf-8')

            f.seek(-symbols_num, 2)
            last_symbols = f.readline().decode('utf-8')

            symbols_list = [first_symbols, mid_symbols, last_symbols]
            print(symbols_list)

    except OSError:
        print('File doesn\'t contain that many characters.')

    return


file = 'file.txt'
symbols_num = int(input('Enter number of characters: '))

symbols(file, symbols_num)
