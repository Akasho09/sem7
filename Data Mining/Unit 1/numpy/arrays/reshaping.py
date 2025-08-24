import numpy as np

arr = np.array([1,2,3,4,5,6])
print(arr.reshape(2,3))
print(arr)

arr2 = arr.reshape(3,2)
print(arr2)
print(arr2.flatten())
print(arr2.ravel())
print(arr2)

