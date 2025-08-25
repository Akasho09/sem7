import numpy as np

# 3. You are given data from a 2D grid of weather sensors placed across a geographic area.
#  Each sensor records the temperature at a given point. 
# The data is stored in a 2D NumPy array `T` of shape `(100, 100)` representing temperature in Celsius.

# You are to perform the following tasks using **only NumPy**:

# #### **Tasks:**

# 1. **Data Initialization:**
#    Simulate the temperature grid `T` by initializing it with random temperature values between 15°C and 45°C.

#    ```python
#    # Example output: array([[22.4, 33.2, ..., 30.1], ..., [28.9, 29.5, ..., 31.2]])
#    ```


# Unifrom means prob is same 
# not Normal (Most values cluster around the mean, fewer at extremes) 

T = np.random.uniform(15, 45, size=(100, 100))
# print(T)

print("Shape of T:", T.shape)
print("Sample values:\n", T[:5, :5])  # show a small top-left portion


print("\n\n")

# 2. **Hotspot Detection:**
#    Define a "hotspot" as any point in the grid whose temperature is more 
# than **10 degrees higher** than the average of its 8 immediate 
# neighbors (N, NE, E, SE, S, SW, W, NW).

#    * Return the (i, j) indices of all hotspot locations.
#    * Use **array slicing and vectorized operations** only.


