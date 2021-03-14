
class Sale:

    def __init__(self, item, quantity):
        self.item = item
        self.quantity = quantity
        self.price = 9.99
        self.total = 0

    def __str__(self):
        return f'A total number of {self.quantity} ordered with a grand total of {self.set_total}'

    def set_total(self):
        self.total = self.price*self.quantity

    def get_total(self):
        return f'The total is : {self.total}'

    def get_quantitty(self):
        return f'Total of {self.quantity} shirts'

    def get_item(self):
        return f'The item is {self.item}'

