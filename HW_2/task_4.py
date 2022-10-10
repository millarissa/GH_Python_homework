"""
Write a script which accepts a <number> from user and then <number> times
asks user for string input.
At the end script must print out result of concatenating
all <number> strings.
"""

user_num = int(input("Number: "))

lines = ""
for i in range(user_num):
    lines += input("String: ")

print ("Concatenated line: ",lines)
