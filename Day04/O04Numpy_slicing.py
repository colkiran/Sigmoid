
import numpy as np

# 1 dimension array
arr = np.array(list(range(1, 11)))
print(f"arr :{arr}")
print(f"Array dimension :{arr.ndim}")

print(f"arr[1:5] :{arr[1:5]}")
print(f"arr[7:]  :{arr[7:]}")
print(f"arr[:5]  :{arr[:5]}")
print(f"arr[:]   :{arr[:]}")
print(f"arr[::2] :{arr[::2]}")

print("-" * 60)

# 2 dimension array

arr1 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9 ,10]])
print(f"arr1 :{arr1}")
print(f"Array dimension :{arr1.ndim}")

print(f"arr1[1, 1:4] :{arr1[1, 1:4]}")
print(f"arr1[0, -1:-5:-1] :{arr1[0, -1:-5:-1]}")
print(f"arr1[1, ::-1]     :{arr1[1, ::-1]}")
print(f"arr1[-1, ::-1]    :{arr1[-1, ::-1]}")

