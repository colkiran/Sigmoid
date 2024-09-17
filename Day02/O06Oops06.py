
class Player:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Player Ctor......")


    def get_details(self):
        print(f"Name is {self.name}\nAge is {self.age}")

    @classmethod
    def ceatePlayer(cls, fn, ln, age):
        # factory
        print("Factory......")
        return cls(f"{fn} {ln}", age)          # call the constructor


ply1 = Player("Virat", 32)
ply1.get_details()

print("-" * 60)

"""
ply2 = first_name, last_name, age

"""
ply2 = Player.ceatePlayer("Sachin", "Tendulkar", 36)
ply2.get_details()
