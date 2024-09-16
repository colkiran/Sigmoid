
def outerFun():
    gname = "Sachin"

    def innerFun():

        print(f"Hello {gname}")

    return innerFun


inref = outerFun()

print("hi")
print("Hello")

inref()             # inner function is called

print("-" * 60)

outerFun()()         # inner function is called

