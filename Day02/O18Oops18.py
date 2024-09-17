
class Animal:

    def __init__(self):
        print("Animal Ctor....")
        self.a = 10

    def eat(self):
        print("Animals eat....")

    def fun(self):
        print("Function fun of class Animal.....")

class Person:

    def __init__(self):
        print("Person Ctor.....")
        self.p = 20


    def talk(self):
        print("Person talks....")

    def fun(self):
        print("Function fun of class Person.....")



class Girl(Animal, Person):

    def __init__(self):
        super().__init__()
        print("Girl Ctor.....")
        self.g = 30

    def walk(self):
        print("Girls walk.....")

grace = Girl()
grace.eat()
grace.walk()
grace.fun()


print(grace.__dict__)








