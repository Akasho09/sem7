import numpy as np

#👉 Stacking = combining multiple arrays into one along a new or existing axis.
# Think of it like putting Lego blocks together:

# Vertical stacking (rows) → one on top of the other . Requres same rows 
# Horizontal stacking (columns) → side by side .  requires same columns 


arr = np.array([1,2,3,4])
arr2 = np.array([4,5,6,9])

print(np.hstack((arr,arr2)))
print(np.vstack((arr,arr2)))
print(np.split(arr,2))


