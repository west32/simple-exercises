# Implement a function that takes as input three variables, and
# returns the largest of the three. Do this without using the Python max() function!
#
# The goal of this exercise is to think about some internals that
# Python normally takes care of for us. All you need is some variables and if statements!

def max_num(a,b,c):
    user_variables= (a,b,c)
    higher_num=0
    for num in user_variables:
        if int(num) > higher_num:
            higher_num=int(num)
    print(higher_num)

max_num(13,646,7889)

#
#
