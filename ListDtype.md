# LIST

EXAMPLES 

>>> tea_varities = ["black" , "green" , "white" , "oolong" ]
>>> print(tea_varities)
['black', 'green', 'white', 'oolong']
>>> print(tea_varities[1])
green
>>> print(tea_varities[-1])
oolong
>>> print(tea_varities[1:3])
['green', 'white']
>>> print(tea_varities[1:])
['green', 'white', 'oolong']
>>> print(tea_varities[3])
oolong


>>> tea_varities[3] = "herbal"
>>> print(tea_varities)
['black', 'green', 'white', 'herbal']

# problem
>>> tea_varities[1:2] ="lemon" # string treated as array
>>> print(tea_varities)
['black', 'l', 'e', 'm', 'o', 'n', 'white', 'herbal']

# solution 
tea_varities = ["black" , "green" , "white" , "oolong" ]
>>> tea_varities[1:2]
['green']
>>> tea_varities[1:2] = ["lemon"]
>>> print(tea_varities)
['black', 'lemon', 'white', 'oolong']

> tea_varities[1:3]=["green" , "hello"]
>>> print(tea_varities)
['black', 'green', 'hello', 'oolong']

print(tea_varities)
['black', 'green', 'hello', 'oolong']
>>> tea_varities[1:1]
[]


>>> tea_varities[1:1] = ["test" , "test" ]
>>> print(tea_varities)
['black', 'test', 'test', 'green', 'hello', 'oolong']


>>> tea_varities[1:2]
['test']
>>> tea_varities[1:3]
['test', 'test']
>>> tea_varities[1:1]
[]
>>> tea_varities[1:3]  ={}
>>> print(tea_varities)
['black', 'green', 'hello', 'oolong']


# LOOP 

>>> tea_varities
['black', 'green', 'hello', 'oolong']
>>> for tea in tea_varities :
...     print(tea)
...     
black
green
hello
oolong

# if 
>>> if "hello" in list:
...     print("i have hello");                                                              
...     
>>> list.append("hello")
>>> print(list)
['gayatri', 'mansi', 'mohit', 'krishna', 'hello']
>>> if "hello" in list:                                                                     
...     print("i have hello");
... 
i have hello
>>> 
>>> list.pop()
'hello'
>>> print(list)
['gayatri', 'mansi', 'mohit', 'krishna']

>>> list.insert(1 , "aditi")
>>> print(list)
['gayatri', 'aditi', 'mansi', 'mohit', 'krishna']



# comprihention 

>>> square = [x**2 for x in range(10)]
>>> square
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]




# -------------------------------------------------


Great! Here's a **complete theoretical explanation of lists in Python**, along with examples to help you understand the concepts better.

---

## 🧠 **Python List – Theory + Examples**

---

### 📘 **1. What is a List?**

A **list** in Python is a built-in **data structure** that can hold an ordered collection of items.  
It is similar to arrays in other languages, but **can store elements of different data types**, such as integers, strings, floats, booleans, or even other lists.

> ✅ **Key features of Python lists:**
- Ordered
- Mutable (can be changed)
- Allow duplicates
- Can hold multiple data types

```python
example = [10, 'hello', 3.14, True]
```

---

### 📘 **2. Creating a List**

There are a few ways to create a list:

```python
# Empty list
empty_list = []

# List of numbers
numbers = [1, 2, 3, 4, 5]

# List of strings
fruits = ['apple', 'banana', 'mango']

# Mixed data types
mixed = [1, 'yes', False, 3.5]

# Using the list() constructor
letters = list('abc')  # ['a', 'b', 'c']
```

---

### 📘 **3. Accessing List Elements**

Python uses **zero-based indexing** (first element is index 0).

```python
fruits = ['apple', 'banana', 'mango']
print(fruits[0])   # apple
print(fruits[-1])  # mango (last element)
```

You can also **slice** a list:
```python
print(fruits[1:3])  # ['banana', 'mango']
```

---

### 📘 **4. Modifying Elements**

Lists are **mutable**, meaning you can change, add, or remove elements.

```python
fruits[1] = 'orange'
print(fruits)  # ['apple', 'orange', 'mango']
```

---

### 📘 **5. List Operations and Methods**

#### 📌 **Basic operations:**
```python
# Concatenation
print([1, 2] + [3, 4])  # [1, 2, 3, 4]

# Repetition
print([1] * 3)          # [1, 1, 1]
```

#### 📌 **Useful methods:**

| Method        | Description |
|---------------|-------------|
| `append(x)`   | Adds `x` to the end |
| `insert(i, x)`| Inserts `x` at index `i` |
| `extend(l)`   | Adds all items from list `l` |
| `remove(x)`   | Removes first occurrence of `x` |
| `pop([i])`    | Removes and returns element at index `i` (last if no index) |
| `clear()`     | Removes all items |
| `index(x)`    | Returns the index of `x` |
| `count(x)`    | Counts occurrences of `x` |
| `sort()`      | Sorts the list in-place |
| `reverse()`   | Reverses the list in-place |
| `copy()`      | Returns a shallow copy |

Example:
```python
nums = [3, 1, 4]
nums.append(2)  # [3, 1, 4, 2]
nums.sort()     # [1, 2, 3, 4]
```

---

### 📘 **6. Looping Through Lists**

```python
# Using for loop
for item in fruits:
    print(item)

# Using index
for i in range(len(fruits)):
    print(fruits[i])
```

---

### 📘 **7. List Comprehension**

A powerful way to create a list in one line.

```python
# Squares of numbers from 0 to 4
squares = [x**2 for x in range(5)]
print(squares)  # [0, 1, 4, 9, 16]
```

---

### 📘 **8. Nested Lists**

Lists inside lists (like a matrix):

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

print(matrix[0])      # [1, 2, 3]
print(matrix[1][2])   # 6
```

---

### 📘 **9. List vs Tuple**

| Feature    | List        | Tuple        |
|------------|-------------|--------------|
| Mutable    | ✅ Yes      | ❌ No        |
| Syntax     | `[ ]`       | `( )`        |
| Performance| Slower      | Faster       |
| Use case   | Changing data | Fixed data |

---

### 🧪 **Practice Exercise (Optional)**

1. Create a list of your 5 favorite movies.
2. Replace the second movie with a new one.
3. Add a new movie to the end of the list.
4. Sort the list alphabetically.
5. Print each movie one by one.

Want me to solve this example too?

Let me know if you want a PDF summary or a mini quiz on lists!