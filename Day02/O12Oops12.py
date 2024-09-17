
class Product:

    def __init__(self, price):
        self.set_price(price)

    def get_price(self):
        return self.__price

    def set_price(self, val):
        if val < 0:
            raise ValueError('Price cannot be less than zero....')
        else:
            self.__price = val


    def del_price(self):
        self.__price = 0


import sys

try:
    pepsi = Product(50)

    print("-" * 60)

    print(pepsi.get_price())

    print("-" * 60)

    pepsi.set_price(85)

    print(pepsi.get_price())

    print("-" * 60)

    pepsi.del_price()

    print(pepsi.get_price())

except:

    print("Exception caught.....")

    print(sys.exc_info()[0])        # exception class

    print(sys.exc_info()[1])        # exception message