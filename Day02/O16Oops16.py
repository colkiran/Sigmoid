
class Animal:

    def __init__(self):
        print("Animal Ctor....")
        self.a = 10

    def eat(self):
        print("Animals eat....")


class Bird(Animal):

    def __init__(self):
        print("Bird Ctor....")
        super().__init__()
        self.b = 20

    def fly(self):
        print("Birds fly....")

cuckoo = Bird()
cuckoo.eat()
cuckoo.fly()

print(cuckoo.__dict__)
