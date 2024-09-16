
def fun(*args):
    return args

print(fun())
print(fun(10))
print(fun(10,20))
print(fun(10, 20, 30))


print("-" * 60)

def add(x, y):
    return x + y


def outerFun(fnc):              # HOF

    def innerFun(*args):
        print("Logged into the resouce.....")
        print(fnc(*args))           # call back
        print("-" * 60)

    return innerFun

addLogger = outerFun(add)
addLogger(30, 50)
