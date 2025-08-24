import numpy as np

arr = np.array([[1,2] , [3,4] , [5,6]])
print(arr)
print(np.insert(arr, 1 , [7,8] , axis=0))
print(np.insert(arr, 1 , [7,8,9] , axis=1))
print(np.insert(arr, 1 , [7,8,9] , axis=None))

print("\n\n")

print(np.append(arr , [7,8]))
arr2 = np.array([[7,8] , [9,10]])
print(np.concatenate((arr, arr2 ) , axis = 0 ))
print(np.concatenate((arr, arr2 ) , axis = None ))
arr2 = np.array([[7,8] , [9,10] , [11,12]])
print(np.concatenate((arr, arr2 ) , axis = 1 )) 

print("\n\n")

print(np.delete(arr2 , 0 ,  axis = 1 )) 
print(np.delete(arr2 , 0 ,  axis = 0 )) 
print(np.delete(arr2 , 0 ,  axis = None )) 


