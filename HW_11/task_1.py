"""
Створити клас Calc, який буде мати атребут last_result та 4 методи.
Методи повинні виконувати математичні операції з 2-ма числами, а саме
додавання, віднімання, множення, ділення.
"""


class Calc:
    """
    Class with attribute last_result
    which returns result of a previous method
    """
    last_result = None
    current_result = None

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def method_addition(self, a, b):
        """Function for adding two numbers"""
        Calc.last_result = Calc.current_result
        Calc.current_result = a + b
        return Calc.current_result

    def method_subtraction(self, a, b):
        """Function for subtraction two numbers"""
        Calc.last_result = Calc.current_result
        Calc.current_result = a - b
        return Calc.current_result

    def method_multiple(self, a, b):
        """Function for multiple two numbers"""
        Calc.last_result = Calc.current_result
        Calc.current_result = a * b
        return Calc.current_result

    def method_division(self, a, b):
        """Function for division two numbers"""
        if b > 0:
            Calc.last_result = Calc.current_result
            Calc.current_result = a / b
        else:
            print('Oops, division by zero is forbidden, result will be None')
            Calc.current_result = None
        return Calc.current_result


print(Calc.__doc__)

x = Calc(4, 6)
print('last_result -->', x.last_result, '\n')

print(x.method_multiple.__doc__)
print(4, "*", 6)
x.method_multiple(4, 6)
print('last_result -->', x.last_result, '\n')

print(x.method_addition.__doc__)
print(1, "+", 1)
x.method_addition(1, 1)
print('last_result -->', x.last_result, '\n')

print(2, "-", 1)
x.method_subtraction(2, 1)
print('last_result -->', x.last_result, '\n')

print(6, "/", 0)
x.method_division(6, 0)
print('last_result -->', x.last_result, '\n')

print(3, "+", 1)
x.method_addition(3, 1)
print('last_result -->', x.last_result)
