import numpy as np

print("\n\n")
arr = np.array([[1,2,3] , [4,5,6] , [7,8,9]])
print(arr+1)
print(arr*2)
print(arr + [10,20,30])
# print(arr+ [[10,20,30] , [20,30,40]]) # error

print("\n\n")

# VECTORISATION

arr = np.array([[1,2,3] , [4,5,6] , [7,8,9]])
arr1 = np.array([[10,20,30] , [40,50,60] , [70,80,90]])
print(arr+arr1)

print("\n\n")

## NANS

arr3 = np.array([1,2,np.nan , 4, np.nan])
print(np.isnan(arr3))
print(arr3[2] == arr3[-1]) # cant compare nan's
print(arr3[2] == arr3[4])
print(np.nan_to_num(arr3)) # default = 0
print(np.nan_to_num(arr3 , nan=10)) # default = 0
arr3 = np.array([1,2, np.inf , 4, -np.inf])
print(np.isinf(arr3))
print(np.nan_to_num(arr3 , posinf=1000 , neginf=-1000))


