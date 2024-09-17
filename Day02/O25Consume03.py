"""
environment variable - sys.path - gives the library path

"""
import sys
# print(sys.path)

sys.path.append("C:\\Delhi")

for pth in sys.path:
    print(pth)

import gurgaon.mymodule as m

m.greet("Kapil Dev")

ply1 = m.Player("Ravi", 32)
print(ply1)


