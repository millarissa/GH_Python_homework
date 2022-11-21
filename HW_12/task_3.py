"""
Створіть клас в якому буде атрибут який буде рахувати
кількість створених екземплярів класів.
"""


class Attributes:

    attribute_counter = 0

    def __init__(self):
        Attributes.attribute_counter += 1


x1 = Attributes()
x2 = Attributes()
print(Attributes.attribute_counter)
