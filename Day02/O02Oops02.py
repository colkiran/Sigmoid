
class Player:

    def __init__(self):         # constructor
        print("Player initialized.......")

    def get_runs(self):
        print("Runs scored.....")


sachin = Player()           # calls __init__ method
sachin.get_runs()

print("-" * 60)

sourav = Player()
sourav.get_runs()

print("-" * 60)
print(isinstance(sachin, Player))
print(isinstance(sachin, object))
print(isinstance(sachin, str))
