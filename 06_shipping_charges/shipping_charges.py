#2/23/2021
#Debra Sparr
#Assignment 6 - shipping rates


"""

The Fast Freight Shipping Company charges the following rates:

Weight of Package

Rate per Pound

$1.50 - 2 pounds or less

$3.00 - Over 2 pounds but not more than 6 pounds

$4.00 - Over 6 pounds but not more than 10 pounds

$4.75 - Over 10 pounds

"""


class ViolatesLawsOfPhysics(Exception):
    pass

def shipping_rates():
    """asks the user to enter the weight of a package and then displays the shipping charge"""
    try:
        # turn input into a float
        weight = float(input('Enter the weight of your package in pounds to get the shipping charge : '))
        # if weight entered is < or = to 0, raise error
        if weight <= 0:
            raise ViolatesLawsOfPhysics
        # Check weight value, display shipping rate for that weight, and look forward to switch statements
        if weight <= 2 and weight > 0 :
            print(f'The shipping charge for a {weight}lb package is $1.50')
        if weight > 2 and weight <= 6 :
            print(f'The shipping charge for a {weight}lb package is $3.00')
        if weight > 6 and weight <= 10 :
            print(f'The shipping charge for a {weight}lb package is $4.00')
        if weight > 10 :
            print(f'The shipping charge for a {weight}lb package is $4.75')
    # catch inputs that cannot be converted to a float
    except ValueError :
        print('You must enter a number to get the shipping weight.')
    # catch input that is less 0
    except ViolatesLawsOfPhysics :
        print('Unless the laws of physics cease to exist in package, your package must have a weight.')


if __name__ == '__main__' :
    shipping_rates()