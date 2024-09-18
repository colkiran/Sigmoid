
gname = "Sachin Tendulkar"

sports = ['cricket', 'football', 'hockey', 'tennis', 'basketball', 'badmiton', 'swimming']

runs = {'test': 18500, 'odi': 23000, 't20': 2500}


def greet(gst):
    print(f"Greeting Mr.{gst}, Welcome to the event.....")


class Player:

    def __init__(self, name, age):
        self.name = name
        self.age = age


    def __str__(self):
        return f"Name is {self.name}\nAge is {self.age}"

print(__name__)

if __name__ == '__main__':

    print(f"gname :{gname}")

    print(f"Sports :{sports}")

    greet("Yuvraj Singh")
