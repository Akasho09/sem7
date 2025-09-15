# Broadcasting is the way NumPy automatically expands arrays of different shapes during arithmetic operations without making copies.
## 1. Basic Rule
- Two arrays are compatible for broadcasting if for each dimension (from right to left):
- They are equal, OR
One of them is 1.
- If compatible → NumPy “stretches” the smaller one.
If not → ValueError.


