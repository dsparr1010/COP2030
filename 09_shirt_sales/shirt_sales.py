# Debra Sparr
# 3/20/21
# Assignment 9 - Shirt Sales OOP

from sale_class import Sale


def create_sale_instance():
    new_sale = Sale('Men medium blue', 65)
    new_sale.set_total()
    print(new_sale)

if __name__ == '__main__':
    create_sale_instance()

