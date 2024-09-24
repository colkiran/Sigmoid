"""
shape = no of elements in each dimension
"""

import numpy as np

arr1 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(f"arr1 :\n{arr1}")

print(arr1.shape)

print("-" * 60)
arr2 = np.array([1, 2, 3, 4], ndmin=5)
print(f"arr2 :{arr2}")
print(f"shape :{arr2.shape}")

# Reshape - convert a one dimension array to 2 dimension
print("-" * 60)
arr1 = np.array(list(range(1, 13)))
print(f"arr1 :{arr1}")

arr2 = arr1.reshape(4, 3)
print(f"arr2 :\n {arr2}")

print("-" * 60)
# one dimension to 3 dimension

arr1 = np.array(list(range(1, 13)))
print(f"arr1 :{arr1}")

arr3 = arr1.reshape(2, 3, 2)
print(f"arr3 :{arr3}")

print("-" * 60)

arr1 = np.array(list(range(1, 9)))
print(f"arr1 :{arr1}")

print(arr1.reshape(2, 4).base)

print("-" * 60)

arr1 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(f"arr1 :{arr1}")
arr2 = arr1.reshape(-1)
print(f"arr2 :{arr2}")
