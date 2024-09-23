
import numpy as np

# o dimension array
arr = np.array(35)

print(f"arr :{arr}")

print(f"Array dimension :{arr.ndim}")

print("-" * 60)

# 1 dimension array

arr1 = np.array([1, 2, 3, 4, 5])

print(f"arr1 :{arr1}")

print(f"Array Dimension :{arr1.ndim}")

print("-" * 60)

# 2 dimension array

arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print(f"arr2 :\n{arr2}")
print(f"Array dimension  :{arr2.ndim}")

print("-" * 60)

# 3 dimension array

arr3 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

print(f"arr3 :\n{arr3}")

print(f"Array dimension :{arr3.ndim}")