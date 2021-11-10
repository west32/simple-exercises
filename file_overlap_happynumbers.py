# Given two .txt files that have lists of numbers in them, find the numbers that are
# overlapping. One .txt file has a list of all prime numbers under 1000, and the other
# .txt file has a list of happy numbers up to 1000.
#
# (If you forgot, prime numbers are numbers that can’t be divided by any other number.
# And yes, happy numbers are a real thing in mathematics - you can look it up on Wikipedia.
# The explanation is easier with an example, which I will describe below.)

with open ("happynumbers.txt","r", encoding="utf-8") as happynumberfile:
    happynumbers= happynumberfile.read()

    print(happynumbers.replace("\n",","))


with open ("primenumbers.txt","r",encoding='utf-8') as primenumbersfile:
    primenumbers= primenumbersfile.read()
    print(primenumbers.replace("\n",","))

overlaping_numbers= []

for number in primenumbers.replace("\n",",").split(","):
    if number in happynumbers.replace("\n",",").split(",") and number not in overlaping_numbers:
        overlaping_numbers.append(int(number))

print(overlaping_numbers)