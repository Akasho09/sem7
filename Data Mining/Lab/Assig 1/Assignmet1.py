import numpy as np

temps = np.array([
    [22, 28, 25],
    [23, 30, 27],
    [21, 29, 24],
    [20, 26, 22],
    [19, 25, 21]
])
# Morning, Afternoon, Evening

# 1. Use axis-wise operations to compute a column of daily average temperatures. 
# Use **hstack** to add the column of daily averages as a fourth column.

# reshape(-1, 1) means “make it a column with 1 col 
# and as many rows as needed.”
avgs = np.mean(temps , axis=1).reshape(-1,1)

result = np.hstack((temps, avgs))

print(result)


# 2. Use axis-wise operations to compute a row of average morning, afternoon and evening temperatures. 
# Use **vstack** to add the row of averages as the last row of the dataset. 
# The last diagonal element should be the overall average of the data.


print("\n New Temps Arrays \n")
colAvgs = np.mean(result , axis=0)
newTemps = np.vstack((result , colAvgs))
print(newTemps)

