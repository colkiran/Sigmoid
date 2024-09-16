
from functools import reduce

l = [5, 8, 2, 6, 10, 3, 7, 9, 1]

print(f"l :{l}")

res = reduce(lambda x, y: x if x < y else y, l)
print(f"res :{res}")

print("-" * 60)

res = reduce(lambda x, y: x + y, l)
print(f"res :{res}")
