
import mymodule

import mymodule as m
from mymodule import greet, Player

print(m.sports)
print(m.runs)

m.greet("Rahul")

print("-" * 60)

greet("Dhoni")

print("-" * 60)

ply1 = Player("Yuvraj", 34)
print(ply1)
