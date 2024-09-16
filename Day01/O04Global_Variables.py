
glbX = 500

def fun(x):         # local variable
    global glbX     # do not assign any value in this line
    print(f"x :{x}")
    glbX = 1000
    print(f"Inside :{glbX}")


print(f"Before call :{glbX}")

fun(15)

print(f"After call :{glbX}")
