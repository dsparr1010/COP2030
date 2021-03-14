# Debra Sparr
# 3/13/2021
# Assignment 8 - Lotto Numbers

import random


def lotto_number():
    """ Program generates lotto numbers based on the number of tickets the user supplies """
    try :
        ticket_number = int(input('How many lotto tickets do you want?'))
        if ticket_number <1 or ticket_number > 8:
            raise ValueError
        master_list = []
        while len(master_list) != ticket_number*6 :
            number = random.randint(1,53)
            if number not in master_list:
                master_list.append(number)
        for i in range(0, len(master_list), 6):
            chunk = master_list[i:i + 6]
            print('Your lotto numbers are :')
            print(chunk)
    except ValueError:
        print('You must enter a number between 1 and 8')

if __name__ == '__main__':
    lotto_number()
