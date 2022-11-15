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

    def method_addition(self):
        """Function for adding two numbers"""
        Calc.last_result = Calc.current_result
        Calc.current_result = self.a + self.b
        return Calc.current_result

    def method_subtraction(self):
        """Function for subtraction two numbers"""
        Calc.last_result = Calc.current_result
        Calc.current_result = self.a - self.b
        return Calc.current_result

    def method_multiple(self):
        """Function for multiple two numbers"""
        Calc.last_result = Calc.current_result
        Calc.current_result = self.a * self.b
        return Calc.current_result

    def method_division(self):
        """Function for division two numbers"""
        if self.b > 0:
            Calc.last_result = Calc.current_result
            Calc.current_result = self.a / self.b
        else:
            print('Oops, division by zero is forbidden, result will be None')
            Calc.current_result = None
        return Calc.current_result


print(Calc.__doc__)

x = Calc(4, 6)
print('last_result -->', x.last_result, '\n')

print(x.method_multiple.__doc__)
x = Calc(4, 6)
print(4, "*", 6)
x.method_multiple()
print('last_result -->', x.last_result, '\n')

print(x.method_addition.__doc__)
x = Calc(1, 1)
print(1, "+", 1)
x.method_addition()
print('last_result -->', x.last_result, '\n')

x = Calc(2, 1)
print(2, "-", 1)
x.method_subtraction()
print('last_result -->', x.last_result, '\n')

x = Calc(6, 0)
print(6, "/", 4)
x.method_division()
print('last_result -->', x.last_result, '\n')

x = Calc(3, 1)
print(3, "+", 1)
x.method_addition()
print('last_result -->', x.last_result)
