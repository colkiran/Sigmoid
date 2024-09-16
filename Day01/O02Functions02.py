
from collections import namedtuple
def arithematicCalc(x, y):
    sum = x + y
    diff = x - y
    prod = x * y
    quot = x / y
    nmdTpl = namedtuple("Arithmetic", "s d p q")
    Arith = nmdTpl(s = sum, d = diff, p = prod, q = quot)
    return Arith

arithObj = arithematicCalc(20, 8)
# print(arithObj)
print(f"Sum  :{arithObj.s}")
print(f"Diff :{arithObj.d}")
print(f"Prod :{arithObj.p}")
print(f"Quot :{arithObj.q}")

