"""
Написати функцію, яка приймає на вхід список (через кому),
підраховує кількість однакових елементів у ньому і
виводить результат. Елементами списку можуть бути
дані будь-яких типів.
"""

def same_in_list(user_list):
    user_list_types = []
    
    for elem in user_list:        
        user_list_types.append(type(elem))
 
    zip_list = list(zip(user_list, user_list_types))

    count_str = ''
    
    for zip_el in zip_list:
        count = zip_list.count(zip_el)
        count_str = count_str + str(zip_el[0]) + '->' + str(count) + '\n'

    list_count = count_str.split("\n")
    
    list_res = [] 

    for i in list_count: 
        if i not in list_res and i: 
            list_res.append(i)

    print(list_res)
    
    return list_res


user_list = [1, 2, 'foo', 'foo', [1, 2], True, 'foo', 1, [1, 2], [1, 4]]
same_in_list(user_list)
