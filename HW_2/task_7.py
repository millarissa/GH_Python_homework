"""
Write a script to concatenate all elements in a list into a string
and print it.
List must include both strings and integers and must be hardcoded.
"""

list_values = [1, 2, 'aaa', 'jjj', 134, 'HFdnfh']

str_from_list = ''.join(str(x) for x in list_values)
print(str_from_list)
