"""
Write a script which accepts a <number> from user and print out a sum
of the first <number> positive integers.
"""

user_num = int(input("Number: "))

sum_numbers = sum(range(0, user_num + 1))
print("Sum of the first", user_num, "positive integers:", int(sum_numbers))
