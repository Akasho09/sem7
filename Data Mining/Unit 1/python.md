

### 1. Printing & Comments

print("Hello, World!")   # Output: Hello, World!
- 
"""
This is a 
multi-line comment
"""

### 2. Variables & Data Types
- Python is `dynamically` typed (no need to declare types).

x = 10            # int
y = 3.14          # float
name = "Akash"    # string
is_happy = True   # boolean

Check type:

print(type(x))   # <class 'int'>

### 3. Taking Input
name = input("Enter your name: ")
print("Hello,", name)

- Note: input() always returns a string.

### 4. Type Conversion
age = int(input("Enter age: "))   # convert to int
pi = float("3.14")                # convert to float


### 5. Operators
#### Arithmetic
print(5 + 2)   # 7
print(5 ** 2)  # 25 (power)
print(5 // 2)  # 2 (floor division)

#### Comparison
print(5 > 2)   # True

#### Logical
print(True and False)  # False



### 6. Strings
s = "Python"
print(s[0])       # P
print(s[-1])      # n
print(s[0:3])     # Pyt (slicing)
print(len(s))     # 6

#### String methods
print(s.lower())      # python
print(s.upper())      # PYTHON
print(s.replace("Py", "My"))   # Mython

- f-strings:

name = "Akash"
age = 21
print(f"My name is {name} and I am {age} years old.")


### 7. Lists (like arrays)
nums = [1, 2, 3, 4]
print(nums[0])      # 1
nums.append(5)      # add
nums.remove(2)      # remove first 2
print(nums[1:3])    # slicing


### 11. Conditionals
x = 10
if x > 0:
    print("Positive")
elif x == 0:
    print("Zero")
else:
    print("Negative")


### 12. Loops
# While loop
i = 1
while i <= 5:
    print(i)
    i += 1

# For loop
for i in range(1, 6):   # 1 to 5
    print(i)

# Looping lists
for item in ["a", "b", "c"]:
    print(item)


# multi dimension array :
A multidimensional array is a collection of elements organized in a structure with more than one dimension