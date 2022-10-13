"""
Write a script which accepts a <number>(int) from user and
generates dictionary in range <number> where key is <number>
and value is <number>*<number>
"""

user_num = int(input('Enter a number: '))

dicts = {}
keys = range(user_num + 1)
for key, value in enumerate(keys):
    value = key**2
    dicts[key] = value

print(dicts)
