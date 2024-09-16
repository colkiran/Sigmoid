
def outerFun(fnc):

    def helperFun(amt):
        print("Logging into the server......")
        fnc(amt)
        print("Logged out of the server.......")
        print("-" * 60)

    return helperFun

@outerFun               # deposit = outerFun(deposit)
def deposit(amt):
    print(f"Amount of {amt} credited into account ending xxxx4569")


deposit(75000)




@outerFun
def withdraw(amt):
    print(f"Amount of {amt} debited from the account ending xxxxx4569")

withdraw(25000)
