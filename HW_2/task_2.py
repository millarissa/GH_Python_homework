"""
Write a script which accepts two sequences of comma-separated
colors from user.
Then print out a set containing all the colors from color_list_1
which are not present in color_list_2.
"""

color_list_1 = input("Enter first sequence of comma-separated colors: ")
color_list_2 = input("Enter second sequence of comma-separated colors: ")

set_1 = set(map(str, color_list_1.split(',')))

set_2 = set(map(str, color_list_2.split(',')))

set_colors = set_1.difference(set_2)
print (set_colors)
