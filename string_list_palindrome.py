# Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string
# that reads the same forwards and backwards.)

word= str(input("enter a string"))
rvs_word = word[::-1]
if word == rvs_word:
    print("That word it is a palindrome..")
else:
    print("This word is not a palind..something")


    # def palind():
    #     my_string = input("Please enter a string: ")
    #
    #
    # return my_string[::] == my_string[::-1]

