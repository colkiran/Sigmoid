
import numpy as np

arr1 = np.array([1, 2, 3, 4])

arr2 = np.array([5, 6, 7, 8])

resarr = np.concatenate((arr1, arr2))

print(resarr)

print("-" * 60)
# 2d array

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])

print(f"arr1 :{arr1}")

print(f"arr2 :{arr2}")

resArr = np.concatenate((arr1, arr2), axis=1)

print(f"resArr :\n{resArr}")

print("-" * 60)
# 2d array

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])

print(f"arr1 :{arr1}")

print(f"arr2 :{arr2}")

resArr = np.stack((arr1, arr2), axis=1)

print()
print(f"resArr :\n{resArr}")

print("-" * 60)

arr1 = np.array([1, 2, 3])
arr2 = np.array([5, 6, 7])

print(f"arr1 :{arr1}")
print(f"arr2 :{arr2}")

resArr = np.hstack((arr1, arr2))

print(f"resArr :{resArr}")

print("-" * 60)

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

print(f"arr1 :{arr1}")
print(f"arr2 :{arr2}")

resArr = np.vstack((arr1, arr2))

print(f"resArr :\n{resArr}")

print("-" * 60)

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

print(f"arr1 :{arr1}")
print(f"arr2 :{arr2}")

resArr = np.dstack((arr1, arr2))

print(f"resArr :\n{resArr}")