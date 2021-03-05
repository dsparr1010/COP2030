"""
Write a program to do the following:

Part 1:

Creates a list with 6 names. The last name is to be used as a ‘sentinel’. Here is an example, but you should use your own names and sentinel
Names = ['Alex', 'Brad', 'Jayne', 'Kim', 'Rafael', 'End']

Implements a ‘while’ loop to display each name as long as the name is not ‘End’ since that is the sentinel
Uses a try/except structure
Part 2:

Manually, not thru the program, please create a text file using mynames.txt as the name. (I will have a file with the same name to test your code. The program should read any number of names).
In the text file, write several names, one per line.

The program then uses ‘while’ loop to read and print the names in the text file, one line at a time
"""

NAMES = ["Aaran", "Aaren", "Aarez", "Aarman", "Aaron", "Aaron-James", "Aarron", "Aaryan", "Aaryn", "Azeem", "End"]
NAMES2 = ["Strachan", "Struan", "Stuart", "Su", "Subhaan", "End", "Sudais", "Suheyb", "Suilven", "Sukhi", "Sukhpal", "Sukhvir"]
NAMES_NO_SENTINEL = ["Aaran", "Aaren", "Aarez", "Aarman", "Aaron", "Aaron-James", "Aarron", "Aaryan", "Aaryn", "Azeem"]

def loop_to_sentinel(names_arr):
    """ Displays each name in the given list, as long as the name is not ‘End’ """
    SENTINEL = 'End'
    try:
        if type(names_arr) != list:
            raise TypeError
        if len(names_arr) == 0 or SENTINEL not in names_arr:
            raise ValueError
        current_number = 0
        while names_arr[current_number] != SENTINEL:
            print(names_arr[current_number])
            current_number += 1
    except TypeError:
        arg_type = type(names_arr)
        print(f'This function requires a list, you passed in {arg_type}!')
    except ValueError:
        print('You passed in a list without any names or did not provide the sentinel (End)!')


loop_to_sentinel(NAMES)
loop_to_sentinel(NAMES2)
loop_to_sentinel(NAMES_NO_SENTINEL)