
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(f'arr :{arr}')
print(arr.dtype)

print("-" * 60)
fruits = np.array(['apple', 'orange', 'banana', 'grapes'])
print(f"fruits :{fruits}")
print(fruits.dtype)

print("-" * 60)
arr1 = np.array([1, 2, 3], dtype="S")
print(f"arr1 :{arr1}")
print(arr1.dtype)

print("-" * 60)
# arr2 = np.array(['a', '10', '20'], dtype='i')
# print(f"arr2 :{arr2}")

arr2 = np.array([7.5, 8.2, 9.9, 3.7])
print(f"arr2 :{arr2}")

arr3 = arr2.astype('i')
print(f"arr3 :{arr3}")
print(arr3.dtype)

print("-" * 60)
arr4 = np.array([2, 1, 0, 4, 0, 5])
print(f"arr4 :{arr4}")

arr5 = arr4.astype(bool)
print(f"arr5 :{arr5}")
print(arr5.dtype)
