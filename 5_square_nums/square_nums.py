#2/16/2021
#Debra Sparr
#Assignment 5 - square numbers and test application

import unittest


# EXAMPLE LISTS :
LIST_NUMB = [1, 20, 13, 10, 5]
LIST_FLOATS = [5.546, 2.0, 4.344, .01]
NOT_LIST_FAIL = 1234
LIST_FAIL = [1, '4', 'asga', True, None]


def square_nums(numbs_list):
    """ Takes a list of numbers and returns each value squared """
    try :
        return list(map( lambda x : x**2, numbs_list))
    except TypeError :
        raise TypeError
    except Exception as err:
        raise Exception(err)

def square_and_display(numbs_list):
    try :
        squared_list = square_nums(numbs_list)
        return f"The original list was {numbs_list}. The new list with values squared in {squared_list}"
    except TypeError :
        return 'The argument must be a list of numbers!'
    except Exception as err:
        return f'An error occurred : {err}.'


class TestSquareNums(unittest.TestCase):
    """ Tests square_nums and square_and_display functions """

    def setUp(self):
        self.LIST_NUMB = LIST_NUMB
        self.LIST_FLOATS = LIST_FLOATS
        self.NOT_LIST_FAIL = NOT_LIST_FAIL
        self.LIST_FAIL = LIST_FAIL

    def test_01_square_numbs_pass(self):
        """ Tests that the square_nums function returns a list with the values squared """
        returned_value = square_nums(self.LIST_NUMB)
        self.assertEqual(returned_value, [1, 400, 169, 100, 25], "Should be a list with equal values")

    def test_05_square_nums_not_list_fail(self):
        """ Tests that an argument that is not a list type will raise a TypeError exception """
        with self.assertRaises(TypeError):
            square_nums(self.NOT_LIST_FAIL)

    def test_10_square_numbs_not_number_types_fail(self):
        """ Tests that elements in a list that are not number types will raise TypeError exception """
        with self.assertRaises(TypeError):
            square_nums(self.LIST_FAIL)

    def test_15_display_pass(self):
        """ Tests that square_and_display returns a string with a list """
        returned_value = square_and_display(self.LIST_NUMB)
        self.assertIn('[' and ']', returned_value, "Should return a string containing opening and closing list brackets")

    def test_20_display_catches_exception(self):
        """ Tests that square_and_display catches TypeError and displays a message """
        returned_value = square_and_display(self.NOT_LIST_FAIL)
        self.assertEqual('The argument must be a list of numbers!', returned_value, "Should catch TypeError raised in square_num and display text")



if __name__ == '__main__':
    print(square_and_display(LIST_NUMB))
    print(square_and_display(LIST_FLOATS))
    print(square_and_display(LIST_FAIL))
    print(square_and_display(NOT_LIST_FAIL))

    #RUN TEST CASES
    print(unittest.main())