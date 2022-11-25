"""
Створити клас Matrix, який буде мати наступний функціонал:
1. __init__ - вводиться кількість стовпців і кількість рядків.
2. fill() - заповнить створений масив числами - по порядку.
3. print_out() - виведе створений масив
(якщо він ще не заповнений даними - вивести нулі)
4. transpose() - перевертає створений масив.
"""


class Matrix:
    def __init__(self, cols, rows):
        self.cols = cols
        self.rows = rows

    def fill(self, fill_list):
        col = self.cols
        row = self.rows
        matrix = []

        for i in range(col):
            matrix.append([])
            for j in range(row):
                if fill_list:
                    matrix[i].append(fill_list[j + row * i])
                else:
                    matrix[i].append(0)

        return matrix

    def print_out(self, matrix):
        print('Matrix with', self.cols, 'cols and', self.rows, 'rows:')
        for i in matrix:
            print(i)

    def transpose(self, matrix):
        col = self.rows
        transposed_matrix = [[row[i] for row in matrix] for i in range(col)]
        print('Reversed matrix: ')
        for i in transposed_matrix:
            print(i)


mat = Matrix(3, 2)
fill_list = [1, 2, 3, 4, 5, 6]
matrix = mat.fill(fill_list)
mat.print_out(matrix)
mat.transpose(matrix)
