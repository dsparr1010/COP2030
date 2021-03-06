#3/6/2021
#Debra Sparr
#Assignment 7 - name printer


NAMES = ["Aaran", "Aaren", "Aarez", "Aarman", "Aaron", "Aaron-James", "Aarron", "Aaryan", "Aaryn", "Azeem", "End"]
NAMES2 = ["Strachan", "Struan", "Stuart", "Su", "Subhaan", "End", "Sudais", "Suheyb", "Suilven", "Sukhi", "Sukhpal", "Sukhvir"]
NAMES_NO_SENTINEL = ["Aaran", "Aaren", "Aarez", "Aarman", "Aaron", "Aaron-James", "Aarron", "Aaryan", "Aaryn", "Azeem"]


# PART 1
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

# PART 2
def name_reader(path):
    """ Reads and prints the names in the text file.

    Argument:
    path : STRING, path to your text file
    """
    try:
        with open(path, 'r') as reader:
            line = reader.readline()
            while line != '':  # Empty string signifies end of document
                print(line, end='')
                line = reader.readline()
    except FileNotFoundError:
        print("You need to pass in the path to your text file.")


if __name__ == '__main__' :
    loop_to_sentinel(NAMES)
    loop_to_sentinel(NAMES2)
    loop_to_sentinel(NAMES_NO_SENTINEL)
    name_reader("") #use path to your text file, as a string, as the argument