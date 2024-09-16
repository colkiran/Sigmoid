
def fun(x):         # x is a local variable
    print(f"x :{x}")
    y = x + 10      # y is a local variable
    print(f"y :{y}")


fun(10)

# print(f"After the function call x :{x}")