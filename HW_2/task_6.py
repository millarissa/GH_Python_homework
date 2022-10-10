"""
Write a script to check whether a value from user input
is contained in a group of values.
"""

values = input("Enter list of values, separated with comma: ")
user_value = input("Enter value: ")

list_values = list(map(str, values.split(',')))
print (user_value in list_values)
