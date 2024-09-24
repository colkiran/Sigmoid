"""
copy - deep copy - changes made to the copied version will not affect the original array
view - shallow copy - changes made to the view will affect the original array
"""

import numpy as np

arr1 = np.array([1, 2, 3, 4, 5])
print(F"arr1 :{arr1}")
arr2 = arr1.copy()

arr1[1] = 200
arr1[4] = 500

print(f"after arr1 :{arr1}")
print(f"after arr2 :{arr2}")

print("-" * 60)
arr3 = np.array([6, 7, 8, 9, 10])
print(f"arr3 :{arr3}")

arr4 = arr3.view()
arr3[0] = 66
arr3[2] = 88
arr3[-1] = 100

print(f"after arr3 :{arr3}")
print(f"after arr4 :{arr4}")


