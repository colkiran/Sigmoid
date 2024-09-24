"""
broadcasting describes how numpy treats arrays with different shapes during arithmatic operations
smaller array is broadcast across larger array, so they have compatible shape

A set of dimension is compatible when
1. one of them has a length of 1
2. they are equal


the smaller dimension array can be appended with 1 in its shape
size of each output dimension is the maximum of the input sizes in the dimension

broadcastable shapes
1. (6, 7) and (6, 7)
2. (6, 7) and (6, 1)
3, (6, 7) and (7, )

Non broadcastable shapes
1. (6, 7) and (7, 6)
2. (6, 7) and (6, )

"""
import numpy as np

arr1 = np.array([1, 2, 3])

arr2 = np.array([[1] , [2], [3]])

print(f"arr1 :{arr1}")
print(f"arr2 ;{arr2}")

resArr = arr1 + arr2

print(f"resArr :\n{resArr}")

print("-" * 60)

arr1 = np.array([1, 2, 3])
print(f"arr1 :{arr1}")

number = 8

resArr = arr1 + number

print(f"resArr :{resArr}")

print("-" * 60)

arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])

print(f"arr1 :{arr1}")
print(f"arr2 :{arr2}")

resArr = arr1 * arr2

print(f"resArr :{resArr}")
