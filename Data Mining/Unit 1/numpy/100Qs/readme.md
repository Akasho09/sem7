# SIZE 

## 2. arr.itemsize
Number of bytes per element, depending on dtype.
Default np.array([1,2,4,4]) uses int64 (on most 64-bit systems).
- So each element = 8 bytes.
- If dtype is int8:
- Each element = 1 byte.

## 4. arr.__sizeof__() 
This shows the total memory footprint of the NumPy object in Python (not just the data).
It includes:
- Array object overhead (~112 bytes, varies by system)
- Data buffer size (size * itemsize)


# 1. In Jupyter Notebook / IPython

`!` is a magic command that means:
👉 “run the rest of the line as a shell command, not Python code.”