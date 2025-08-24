import numpy as np

# astype
arr = np.array([1 , 2.0 , 3.8 , 4.5 ])
print(arr.dtype)
print(arr.astype(int).dtype)
print(np.sum(arr))
print(np.sum(arr.astype(int)))

# maths on arrays
arr2 = np.array([1 ,2 , 3 , 4  ])
print(arr2*3)
print(arr2**2)
print(np.sum(arr2))
print(np.mean(arr2))
print(np.median(arr2))
print(np.max(arr2))
print(np.std(arr2))
print(np.var(arr2))


## Indexing and slicing in np


# ---------------- 1D Array ----------------
arr1d = np.array([10, 20, 30, 40, 50])

# Indexing
print(arr1d[0])    # 10   (first element)
print(arr1d[-1])   # 50   (last element)

# Slicing
print(arr1d[1:4])  # [20 30 40]  (from index 1 to 3)
print(arr1d[:3])   # [10 20 30]  (first 3 elements)
print(arr1d[2:])   # [30 40 50]  (from index 2 to end)
print(arr1d[::2])  # [10 30 50]  (every 2nd element)
print(arr1d[::-1]) # [50 40 30 20 10]  (reverse)

# ---------------- 2D Array ----------------
arr2d = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

# Indexing
print(arr2d[0, 1])   # 2  (row 0, col 1)
print(arr2d[-1, -1]) # 9  (last row, last col)

# Slicing rows/columns
print(arr2d[0:2, :])  # first 2 rows, all cols
print(arr2d[:, 1])    # all rows, column 1 -> [2 5 8]
print(arr2d[1, :])    # row 1 -> [4 5 6]

# ---------------- 3D Array ----------------
arr3d = np.array([[[1,2],[3,4]],
                  [[5,6],[7,8]]])

# Indexing
print(arr3d[0, 1, 1])  # 4  (block 0, row 1, col 1)
print(arr3d[:, 0, 1])  # [2 6]  (all blocks, first row, 2nd col)

# Slicing
print(arr3d[:, :, 0])  # first column of all blocks



# FANCY INDEXING

arr = np.array([10, 20, 30, 40, 50])

# Select elements at positions 0, 2, 4
fancy = arr[[0, 2, 4]]
print(fancy)  # [10 30 50]

# 2D example
arr2d = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

# Select rows 0 and 2
rows = arr2d[[0, 2], :]
print(rows)
# [[1 2 3]
#  [7 8 9]]

# Select specific elements: (row 0,col1), (row1,col2), (row2,col0)
elements = arr2d[[0,1,2], [1,2,0]]
print(elements)  # [2 6 7]



# FILTERING 

arr = np.array([10, 20, 30, 40, 50])

# Filter elements greater than 25
filtered = arr[arr > 25]
print(filtered)  # [30 40 50]

# Multiple conditions
filtered = arr[(arr > 15) & (arr < 45)]
print(filtered)  # [20 30 40]

# 2D example
arr2d = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])
print(arr2d[arr2d % 2 == 0])  # [2 4 6 8] (even numbers)




print(np.linspace(0, 10, num=4))
# np.linspace(start, stop, num) → returns num evenly spaced values between start and stop inclusive.
