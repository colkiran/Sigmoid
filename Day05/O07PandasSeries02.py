
import pandas as pd

a = [1, 2, 3, 4, 5]

mySeries = pd.Series(a)

print(f"mySeries :\n{mySeries}")

print(type(mySeries))

print("-" * 60)

print(f"mySeries[2] :{mySeries[2]}")

print("-" * 60)

mysrs = pd.Series(a, index = ['a', 'b', 'c', 'd', 'e'])
print(f"mysrs :\n{mysrs}")

print("-" * 60)
print(mysrs['a'])
print(mysrs['c'])
print(mysrs['e'])
