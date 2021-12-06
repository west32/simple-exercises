# ZADANIE 2. PODANA JEST LISTA ZAWIERAJĄCA ELEMENTY O WARTOŚCIACH 1-n.
# NAPISZ FUNKCJĘ KTÓRA SPRAWDZI JAKICH ELEMENTÓW BRAKUJE
#
# 1-n = [1,2,3,4,5,...,10]
# np. n=10
# wejście: [2,3,7,4,9], 10
# wyjście: [1,5,6,8,10]
import random


def missing_elements(list,n):

    missing_elements_list=[]
    range_list = [value for value in range(1, n + 1)]
    for number in range_list:
        if number not in list:
            missing_elements_list.append(number)
    return missing_elements_list

def run_exercise_two():

    print(f"Elementy brakujące to: {missing_elements([1, 2, 9, 7],10)}")

if __name__=="__main__":
    run_exercise_two()