
class Sale:

    def __init__(self, item, quantity):
        self.item = item
        self.quantity = quantity
        self.price = 9.99
        self.total = 0

    def __str__(self):
        return f'A total number of {self.quantity} {self.item} ordered, with a grand total of ${self.total}'

    def set_total(self):
        ''' A method to calculate the total '''
        self.total = round(self.price*self.quantity, 2)
        return

    def get_total(self):
        ''' A method to return the total '''
        return f'The total is : {self.total}'

    def get_quantity(self):
        ''' A method to return quantity'''
        return f'Total of {self.quantity} shirts'

    def get_item(self):
        ''' A method to return the item '''
        return f'The item is {self.item}'

