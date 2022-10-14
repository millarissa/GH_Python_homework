"""
Write a script to get the maximum and minimum VALUE
in a dictionary.
"""

dict_1 = {1: 43, 2: 85, 3: 'asdfg', 4: 3411, 5: 1}

dict_2 = {}
for key,value in dict_1.items():
    if type(value) == int:
        dict_2[key] = value

dict_values = dict_2.values()
        
max_val = max(dict_values)
min_val = min(dict_values)

print('Maximum value: ', max_val)
print('Minimum value: ', min_val)



