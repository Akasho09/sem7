import numpy as np 
temperatures = [10.2 , 30.2 , 0 , 15 , 78 ]

total = 0 

for temp in temperatures:
    total+=temp

print(total/len(temperatures))


temps = np.array([
    [22, 28, 25],
    [23, 30, 27],
    [21, 29, 24],
    [20, 26, 22],
    [19, 25, 21]
])

av = np.mean(temps)
print(av)