
import numpy as np

# 1 dimension array

arr = np.array([1, 2, 3, 4, 5])

print(f"arr :{arr}")

print(f"Array dimension :{arr.ndim}")

print(f"arr[0] :{arr[0]}")
print(f"arr[3] :{arr[3]}")
print(f"arr[-1] :{arr[-1]}")

print(f"arr[1] + arr[4] :{arr[1] + arr[4]}")

print("-" * 60)

# 2 dimension Array
arr1 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(f"arr1 :\n{arr1}")
print(f"Array dimension :{arr1.ndim}")

# extracting data
print(f"arr1[0, 2] :{arr1[0, 2]}")
print(f"arr1[1, 3] :{arr1[1, 3]}")

print("-" * 60)

# 3 dimension Array

arr2 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(f"arr2 :\n{arr2}")
print(f"Array dimension :{arr2.ndim}")

print(f"value 2 :{arr2[0, 0, 1]}")
print(f"value 11 :{arr2[1, 1, 1]}")



