
def add(x, y):
    return x + y


# print(add(56, 93))

a = add
print(a(18, 32))

print("-" * 60)

l = lambda x, y: x + y
print(l(39, 57))

print("-" * 60)
l = list(range(1, 11))
squares = list(map(lambda x: x ** 2, l))

print(f"res :{squares}")

