# Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only
# the first and last elements of the given list. For practice, write this code inside a function.

a = [5, 10, 15, 20, 25]

def first_and_last(list):
    first_num= list[0]
    last_num= list[-1]
    new_list = [first_num,last_num]
    return new_list

# or

def list_ends(list):
    return [list[0],list[-1]]

