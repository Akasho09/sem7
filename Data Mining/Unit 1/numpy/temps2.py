import numpy as np


temps = np.array([
    [22, 28, 25],
    [23, 30, 27],
    [21, 29, 24],
    [20, 26, 22],
    [19, 25, 21]
])

av = np.mean(temps)
print(av)


temps2= [
    [22, 28, 25],
    [23, 30, 27],
    [21, 29, 24],
    [20, 26, 22],
    [19, 25, 21]
]

total = 0

for t in temps2:
    for ti in t:
        total+=ti

print(total/(len(temps2)*len(temps2[0])))

avg = sum(sum(row) for row in temps2) / sum(len(row) for row in temps2)
print(avg)  # 24.1333...
