# Debra Sparr
# 4/25/21
# Assignment 12 - Option 1 - Recursion

''' The deliver_presents_recursively function is a function to help Santa deliver presents to children. It is a recursive function because it
    invokes itself from inside the function repeatedly until some condition is met (in this case, that would be all the houses being
    iterated over). The function divides the problem into subproblems (lines 29 & 30) to execute and finish the problem. '''

houses = ["Eric's house", "Kenny's house", "Kyle's house", "Stan's house"]

# Each function call represents an elf doing his work
def deliver_presents_recursively(houses):
    # Worker elf doing his work
    # If length of houses can no longer be divided in half anymore, print delivery statement
    if len(houses) == 1:
        house = houses[0]
        print("Delivering presents to", house)

    # Santa divvying up tasks to elves
    else:
        # Cut the list of houses in two
        mid = len(houses) // 2
        # Get list of first half of houses
        first_half = houses[:mid]
        # Get list of second half of houses
        second_half = houses[mid:]

        # Santa divides his work among two elves
        deliver_presents_recursively(first_half)
        deliver_presents_recursively(second_half)


if __name__ == '__main__':
    deliver_presents_recursively(houses)