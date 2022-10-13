""" Write a script to remove empty elements from a list. """

list_test = [
    (), ('hey'), ('',), ('ma', 'ke', 'my'),
    [''], {}, ['d', 'a', 'y'], '', []
]

list_res = []
for list_elem in list_test:
    if list_elem:
        list_res.append(list_elem)

print(list_res)


