
def greet():
    print("Greetings Mr.Sachin, Welcome to the event.....")


def greetGst(gname):
    print(f"Greetings Mr.{gname}, Welcome to the event......")


# city - default argument,  gname is called non default argument
# def greetGstCty(gname, x, city="Mumbai"):
def greetGstCty(gname,  city="Mumbai"):
    print(f"Greetings Mr.{gname} from {city}, Welcome to the event......")

greet()

print("-" * 60)

greetGst("Sachin")
greetGst("Rahul")

print("-" * 60)

greetGstCty("Sunil")
greetGstCty("Rohit")
greetGstCty("Rahul", "Bangalore")

print("-" * 60)

def admission(fname, lname, dob, city, qlf, gender, adr, conno):
    print(f"Name is         :{fname} {lname}")
    print(f"DOB             :{dob}")
    print(f"City            :{city}")
    print(f"Qualification   :{qlf}")
    print(f"Gender          :{gender}")
    print(f"Address         :{adr}")
    print(f"Contact No      : {conno}")

admission(city = "Chennai",gender="Male", dob = "15/07/1992", fname = "Rahul", lname = "Dravid", conno="237423948", qlf="B.E", adr = "#145, 5th Cross, 8th Main, MG Road, Bangalore")

print("-" * 60)
# variable length arguments - *args and **kwargs
def multiplyMe(*numbers):
    print(f"numbers :{numbers}")
    print("*numbers :", *numbers)       # unpack
    prod = 1
    for number in numbers:
        prod *= number
    return prod

res = multiplyMe(1, 2, 3, 4, 5)
print(f"res :{res}")

print("-" * 60)
def acceptMe(**details):
    print("details :", details)
    print("-" * 60)
    for k, v in details.items():
        print(k, "=>", v)


acceptMe(name="Sachin", age=32, runs=182, oppn="WI", Venue="Sabina Park", year=2016)

print("-" * 60)

def arithematicCalc(x, y):
    sum = x + y
    diff = x - y
    prod = x * y
    quot = x / y
    return sum, diff, prod, quot

res = arithematicCalc(20, 8)
print(f"res :{res}")

print("-" * 60)

def fun():
    # this is a comment
    "This is a doc string"
    print("Hello World")


fun()

print("-" * 60)

print(fun.__doc__)

print("-" * 60)

def fun1(x, y):
    """
    fun1(x, y)
    ----------

     1. if fun1 takes x and y as integer then the result is the sum of x and y
     2. if fun1 takes x and y as strings then the result is the concatenation of the string x and y
     3. if fun1 takes x as integer and y as a string then it throws an error.

    """
    return x + y

print(fun1(34, 78))

print("-" * 60)

print(fun1("Hello ", "World"))

print("-" * 60)

help(fun1)