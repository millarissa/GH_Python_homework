"""
Write a script to get the maximum and minimum VALUE
in a dictionary.
"""

dict_1 = {1: 25, 2: 58, 3: 33341, 4: 12}

dict_values = dict_1.values()
max_val = max(dict_values)
min_val = min(dict_values)

print('Maximum value: ', max_val)
print('Minimum value: ', min_val)
