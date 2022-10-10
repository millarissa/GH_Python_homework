"""
Write a script which accepts a sequence of comma-separated numbers from
user and generates a list and a tuple with those numbers.
"""

user_nums = input("Enter sequence of comma-separated numbers: ")

num_list = list(map(int, user_nums.split(', ')))
print("List: ", num_list)

num_tuple = tuple(map(int, user_nums.split(', ')))
print("Tuple:", num_tuple)




