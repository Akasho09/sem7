import numpy as np

# ----------------  ----------------
print(" Arrays In Numpy  \n")

zerosArr = np.zeros((2,3))
print(zerosArr)

onesArr = np.ones((3,2))
print(onesArr)

filledArr = np.full((2,3) , 9)
print(filledArr)

rangeArr = np.arange(2,20,3) # start(included) ,  stop(excluded) , jump
print(rangeArr)

IdentityMatrix = np.eye(4)
print(IdentityMatrix)


print("\n")


# ---------------- 1D Array ----------------
arr1d = np.array([1, 2, 3, 4, 5])
print("1D array:", arr1d)
print("Shape:", arr1d.shape) # no of elemnts
print("Size:", arr1d.size)
print("Sum:", np.sum(arr1d)) # FUNCTION
print("Sum 2 :", arr1d.sum()) # METHOD
print("Mean:", np.mean(arr1d))

# ---------------- 2D Array ----------------
arr2d = np.array([[1, 2, 3 ],
                  [4, 5, 6],
                  [7, 8, 9]])
print("\n2D array:\n", arr2d)
print("Shape:", arr2d.shape)
print("Size:", arr2d.size)
print("Row-wise sum:", np.sum(arr2d, axis=1))
print("Column-wise sum:", np.sum(arr2d, axis=0))
print("Row-wise mean:", np.mean(arr2d, axis=1))
print("Column-wise mean:", np.mean(arr2d, axis=0))

# Add a new column (e.g., daily average)
daily_avg = np.mean(arr2d, axis=1).reshape(-1, 1)
arr2d_aug = np.hstack((arr2d, daily_avg))
print("\n2D array with daily average:\n", arr2d_aug)

# ---------------- 3D Array ----------------
arr3d = np.array([[[1,2],[3,4]],
                  [[5,6],[7,8.0]],
                  [[9,10],[11,12]]])
print("\n3D array:\n", arr3d)
print("Shape:", arr3d.shape)
print("Data Type:", arr3d.dtype)
print("Dimensions:", arr3d.ndim) # 3d array

# Sum along different axes
print("Sum over all elements:", np.sum(arr3d))
print("Sum along axis=0:\n", np.sum(arr3d, axis=0))
print("Sum along axis=1:\n", np.sum(arr3d, axis=1))
print("Sum along axis=2:\n", np.sum(arr3d, axis=2))
