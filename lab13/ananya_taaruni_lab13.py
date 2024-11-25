import numpy as np


arr = np.zeros((4, 6), dtype=int)
print()
print()
print("Shape of the array: ", arr.shape)
print("Size of the array: ", arr.size)

arr = np.insert(arr, 2, 7, axis=0)
print("\nArray after step-3:\n", arr)

arr = np.insert(arr, 0, 2, axis=1)
print("\nArray after step-4:\n", arr)

arr = np.sort(arr, axis=1)
print("\nArray after step-5:\n", arr)

arr = np.resize(arr, (7, 5))
print("\nArray after step-6:\n", arr)

flat_arr = arr.flatten(order='F')
print("\nArray after step-7:", flat_arr)

ones_arr = np.ones(35, dtype=int)
result = flat_arr + ones_arr
print("\nAfter step-8:", result)
print()