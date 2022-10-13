""" Write a script to remove values duplicates from dictionary. """

dict_1 = {1: 'foo', 2: 'bar', 3: 'bar', 4: 'baz'}

result = {}
for key,value in dict_1.items():
    if value not in result.values():
        result[key] = value

print(result)
