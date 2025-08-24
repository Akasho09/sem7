import numpy as np

arr = np.array([1,2,3,4])
arr2 = np.array([4,5,6,9])

print(np.hstack((arr,arr2)))
print(np.vstack((arr,arr2)))
print(np.split(arr,2))


