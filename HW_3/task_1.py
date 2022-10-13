"""
Write a script that will run through a list of tuples and replace
the last value for each tuple.
The list of tuples can be hardcoded.
The "replacement" value is entered by user.
The number of elements in the tuples must be different.
"""

list_tuples = [(1,2,3), ('S','P','Q','R'), ('a','b'), (8, 7, 6, 5, 4)]
change_val = input('Enter replacement value: ')

for i,tuples in enumerate(list_tuples):
    tup_list = list(list_tuples[i])
    tup_list[-1] = change_val
    list_tuples[i] = tuple(tup_list)
    
print(list_tuples)
