#2/5/2021
#Debra Sparr
#Assignment 1 - unit_conversion

def unit_conversion():
    """ Converts Fahrenheit to Celsius """
    degree_sign= u'\N{DEGREE SIGN}'

    try :
        user_input = float(input("Enter number of degrees in Fahrenheit to covert it to Celsius : "))
        cel = (user_input -32)*5/9
        print(f'{str(user_input)}{degree_sign} Fahrenheit is {str(round(cel, 2))}{degree_sign} Celsius')
    except ValueError :
        print("You must enter a whole number or decimal to convert to Celsius.")



if __name__ == '__main__' :
    unit_conversion()