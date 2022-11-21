"""
Напишіть програму, де клас «геометричні фігури» (Figure)
містить властивість color з початковим значенням white
і метод для зміни кольору фігури,
а його підкласи «овал» (Oval) і «квадрат» (Square)
містять методи _init_ для завдання початкових розмірів об'єктів при їх створенні.
"""

import math


class Figure:
    color = 'White'

    def change_color(self, new_color):
        self.color = new_color
        return new_color


class Oval(Figure):

    def __init__(self, minor_axe, major_axe):
        self.minor_axe = minor_axe
        self.major_axe = major_axe

    def size(self):
        size = math.pi * self.major_axe * self.minor_axe
        print(self.color, 'Oval is', size, 'cm2')
        return size


class Square(Figure):

    def __init__(self, side_len):
        self.side_len = side_len

    def size(self):
        size = self.side_len * 4
        print(self.color, 'Square is', size, 'cm2')
        return size


square = Square(4)
square.size()

oval = Oval(2, 4)
new_color = 'Red'
oval.change_color(new_color)
oval.size()
