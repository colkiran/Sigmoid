
class Product:

    def __init__(self, price):
        self.__price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, val):
        self.__price = val

    @price.deleter
    def price(self):
        self.__price = 0


fanta = Product(45)
print(fanta.price)

del fanta.price
print(fanta.price)

fanta.price = 60
print(fanta.price)