#! c:\python

print("Hello World")
print("Hello World")
print("Hello World")

"""
print("Hello World")
print("Hello World")
print("Hello World")
print("Hello World")
"""

print("-" * 60)

def fun():
    # function code
    for i in range(1, 31):
        # for loop code
        if i % 3 == 0:
            # if cond code
            print(i, end=" ")
        print("*", end=" ")
    print("\nHello World")


# main module code
fun()