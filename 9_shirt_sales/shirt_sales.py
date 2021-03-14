# Debra Sparr
# 3/16/21
# Assignment 9 - Shirt Sales OOP


"""
Assume you sell t-shirts ( or any other item), and all t-shirts cost the same, they all have the same price

Define a class called Sale. The first line of the constructor would only have 3 arguments: self, item and quantity. In addition, the constructor has 
an attribute for the price and an attribute to hold the total for the sale.

The program assumes the same price for every item, so you can initialize the price in __init__ using the price of your choice. 
Just like we did with the car example I showed in the lecture, where the speed attribute was initialized to zero in __init__, you could initialize  total at total to zero

The class should have 4 methods to:

A method to calculate the total
A method to return the total
A method to return the item
A method to return quantity
The program importing the file with this class needs to create an instance of the Sale class. Assuming, 
the file with the class definition is sale.py and the class is Sale, it would look something like this

new_sale = sale.Sale('Men medium blue', 10)

When I run the program that creates the class instance, assuming the price in the class was set to 9.99, the output would look something like this

new_sale = sale.Sale('Men medium blue', 10)

>>>

The total for 10 t-shirts  Men medium blue is $ 99.9

>>>
"""


from sale_class import Sale

