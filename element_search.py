# Write a function that takes an ordered list of numbers (a list where
# the elements are in order from smallest to largest) and another number.
# The function decides whether or not the given number is inside the
# list and returns (then prints) an appropriate boolean.


import random


random_list= [random.randint(0,100) for number in range (0,20)]
random_list.sort()


def is_that_number_in_list(list):
    number=int(input("is this number in list? : "))
    return print(f"{number in list}")

print(random_list)
is_that_number_in_list(random_list)