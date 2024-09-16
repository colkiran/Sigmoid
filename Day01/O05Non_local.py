

def outerFun():
    gname = "Sachin"

    def innerFun():

        nonlocal gname    # only local variables can be converted into nonlocal
        gname = gname + ' Tendulkar'
        print("hello world")
        print(f"Greetings Mr.{gname}")


    innerFun()
    print(f"Outer function :{gname}")

outerFun()