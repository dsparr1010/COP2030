#2/5/2021
#Debra Sparr
#Assignment 2 - input summation

from functools import reduce


def input_summation():
    """ Sum a series of numbers entered by the user """

    try :
        numbers_list = []
        num_of_elements = int(input("How many numbers to you want to add together? "))
        if num_of_elements <= 0 :
            print('The number of elements you would like to add together must be a positive integer')
            return
        while len(numbers_list) < num_of_elements :
            numbers_list.append(int(input("Enter numbers ")))
        total = reduce(lambda curr, acc : curr + acc, numbers_list)
        print(f'The total summation of numbers entered is : {total}')
    except ValueError:
        print("Please enter a number")



if __name__ == '__main__' :
    input_summation()