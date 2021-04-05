# Debra Sparr
# 4/4/21
# Assignment 10 - State Capitals

''' Write a program that creates 2 dictionaries: a dictionary containing the U.S. states as keys and
their capitals as values (Use the provided list of states and capitals. Copy and paste them to your code ).
The second dictionary contains the U.S. states as keys and the population as values. (You can make the numbers
for the population up). The program should ask the user for the name of a state and based on the state name,
display the capital and the state’s population. For instance, if the user types ‘Arizona’, the program
should display something like:

The capital of Arizona is Phoenix with a population of 6,927,347
'''

STATES_AND_CAPITALS = {'Alabama':'Montgomery', 'Alaska':'Juneau',
'Arizona':'Phoenix', 'Arkansas':'Little Rock',
'California':'Sacramento', 'Colorado':'Denver',
'Connecticut':'Hartford', 'Delaware':'Dover',
'Florida':'Tallahassee', 'Georgia':'Atlanta',
'Hawaii':'Honolulu', 'Idaho':'Boise',
'Illinois':'Springfield', 'Indiana':'Indianapolis',
'Iowa':'Des Moines', 'Kansas':'Topeka',
'Kentucky':'Frankfort', 'Louisiana':'Baton Rouge',
'Maine':'Augusta', 'Maryland':'Annapolis',
'Massachusetts':'Boston', 'Michigan':'Lansing',
'Minnesota':'Saint Paul', 'Mississippi':'Jackson',
'Missouri':'Jefferson City', 'Montana':'Helena',
'Nebraska':'Lincoln', 'Nevada':'Carson City',
'New Hampshire':'Concord', 'New Jersey':'Trenton',
'New Mexico':'Santa Fe', 'New York':'Albany',
'North Carolina':'Raleigh', 'North Dakota':'Bismarck',
'Ohio':'Columbus', 'Oklahoma':'Oklahoma City',
'Oregon':'Salem', 'Pennsylvania':'Harrisburg',
'Rhode Island':'Providence', 'South Carolina':'Columbia',
'South Dakota':'Pierre', 'Tennessee':'Nashville',
'Texas':'Austin', 'Utah':'Salt Lake City',
'Vermont':'Montpelier', 'Virginia':'Richmond',
'Washington':'Olympia', 'West Virginia':'Charleston',
'Wisconsin':'Madison', 'Wyoming':'Cheyenne'}

STATE_AND_POPULATIONS = {'Alabama':'4,903,185', 'Alaska':'731,545',
'Arizona':'7,278,717', 'Arkansas':'3,017,804',
'California':'39,512,223', 'Colorado':'5,758,736',
'Connecticut':'3,565,287', 'Delaware':'973,764',
'Florida':'21,477,737', 'Georgia':'10,617,423',
'Hawaii':'1,415,872', 'Idaho':'1,787,065',
'Illinois':'12,671,821', 'Indiana':'6,732,219',
'Iowa':'3,155,070', 'Kansas':'2,913,314',
'Kentucky':'4,467,673', 'Louisiana':'4,648,794',
'Maine':'1,344,212', 'Maryland':'6,045,680',
'Massachusetts':'6,892,503', 'Michigan':'9,986,857',
'Minnesota':'5,639,632', 'Mississippi':'2,976,149',
'Missouri':'6,137,428', 'Montana':'1,068,778',
'Nebraska':'1,934,408', 'Nevada':'3,080,156',
'New Hampshire':'1,359,711', 'New Jersey':'8,882,190',
'New Mexico':'2,096,829', 'New York':'19,453,561',
'North Carolina':'10,488,084', 'North Dakota':'762,062',
'Ohio':'11,689,100', 'Oklahoma':'3,956,971',
'Oregon':'4,217,737', 'Pennsylvania':'12,801,989',
'Rhode Island':'1,059,361', 'South Carolina':'5,148,714',
'South Dakota':'884,659', 'Tennessee':'6,829,174',
'Texas':'28,995,881', 'Utah':'3,205,958',
'Vermont':'623,989', 'Virginia':'8,535,519',
'Washington':'7,614,893', 'West Virginia':'1,792,147',
'Wisconsin':'5,822,434', 'Wyoming':'578,759'}


def get_capital_and_population():
    ''' Ask user for the name of a state and displays the capital and the state’s population. '''

    state = input('Enter a state : \n').capitalize()
    if state not in STATES_AND_CAPITALS:
        raise TypeError('You entered a state that is not in the dictionary.')
    capital = STATES_AND_CAPITALS[state]
    population = STATE_AND_POPULATIONS[state]
    print(f'The capital of {state} is {capital} with a population of {population}.')

if __name__ == '__main__':
    get_capital_and_population()

