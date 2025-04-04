# Tuples 

>>> types = (1,2,3,4,5)
>>> types
(1, 2, 3, 4, 5)
>>> types[2]
3
>>> types[-2]
4
>>> types[1:3]
(2, 3)
>>> types[0] = "one"
Traceback (most recent call last):
  File "<python-input-48>", line 1, in <module>
    types[0] = "one"
    ~~~~~^^^
TypeError: 'tuple' object does not support item assignment
>>> 


>>> types2 = (11,22,33,44,55)
>>> all = types + types2
>>> 
>>> all
(1, 2, 3, 4, 5, 11, 22, 33, 44, 55)


>>> if 11 in all : 
...     print("11")
... 
11




>>> if 11 not in all : 
...     print("11")
... 
>>> for i in all:
...     print(i)
... 
1
2
3
4
5
11
22
33
44
55


>>> len(all)
10

>>> min(all)
1

>>> max(all)
55

>>> sum(all)
275

>>> types = (1,2,3,4,5)
>>> types[0:3] = ("one", "two", "three")
Traceback (most recent call last):
  File "<python-input-54>", line 1, in <module>
    types[0:3] = ("one", "two", "three")
    ~~~~~^^^
TypeError: 'tuple' object does not support item assignment

Accept suggestion 1
Suggestion 2
>>> if 11 not in all : 
...     print("11")
... 
>>> 
>>> len(all)
10
>>> 
>>> min(all)
1
>>> max(all)
55
>>> 
>>> sum(all)
330
>>> 
>>> del types2
>>> types2
Traceback (most recent call last):
  File "<python-input-61>", line 1, in <module>
    types2
NameError: name 'types2' is not defined

Accept suggestion 2
Suggestion 3
>>> if 11 not in all : 
...     print("11")
... 
>>> len(all)
10
>>> all.count(2)
1
>>> all.index(2)
1
>>> all.index(22)
6
>>> all.index(100)
Traceback (most recent call last):
  File "<python-input-77>", line 1, in <module>
    all.index(100)
ValueError: tuple.index(x): x not in tuple

Accept suggestion 3
Suggestion 4
>>> if 100 in all : 
...     print("100")
... 
>>> 
>>> for i in all:
...     print(i)
... 
1
2
3
4
5
11
22
33
44
55

>>> len(all)
10


>>> types3 = (1,2,3,4,5)
>>> types4 = (1,2,3,4,5)
>>> types3 == types4
True

>>> types5 = (1,2,3,4,"a")
>>> types6 = (1,2,3,4,"b")
>>> types5 == types6
False

Accept suggestion 4
Suggestion 5
>>> if 88 in all : 
...     print("88")
... 
>>> 
>>> for i in all:
...     print(i, end=' ')
... 
1 2 3 4 5 11 22 33 44 55 

>>> len(all)
10

>>> types.count(1)
1

>>> types.index(3)
2

>>> types.index(100)
Traceback (most recent call last):
  File "<python-input-61>", line 1, in <module>
    types.index(100)
ValueError: tuple.index(x): x not in tuple
>>>

Accept suggestion 5
Suggestion 6
>>> if 111 in all : 
...     print("111")
... 
>>> 
>>> if 1 not in all : 
...     print("1 not in all")
... 
1 not in all

>>> for i in types:
...     print(i)
... 
1
2
3
4
5

>>> for i in types2:
...     print(i)
... 
11
22
33
44
55


>>> len(all)
10

Accept suggestion 6
Suggestion 7
>>> if 99 in all : 
...     print("99")
... 
>>> 
>>> len(all)
10
>>> all.count(2)
1
>>> all.index(3)
2
>>> all.index(99)
Traceback (most recent call last):
  File "<python-input-57>", line 1, in <module>
    all.index(99)
ValueError: tuple.index(x): x not in tuple

>>> types = (1,2,3,4,5)
>>> types[0:3] = 100,200,300
Traceback (most recent call last):
  File "<python-input-59>", line 1, in <module>
    types[0:3] = 100,200,300
TypeError: 'tuple' object does not support item assignment

>>> # Tuples are immutable.

Accept suggestion 7
Suggestion 8
>>> if 11 in types : 
...     print("11")
... 
>>> 
>>> for i in all : 
...     print(i)
... 
1
2
3
4
5
11
22
33
44
55
>>> 

>>> len(all)
10


>>> tuple1 = (1,2,3,4,5)
>>> tuple2 = (6,7,8,9,10)
>>> tuple3 = tuple1 + tuple2
>>> tuple3 = tuple3 * 2 # Repeats the elements of the tuple 2 times.
>>> tuple3
(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

Accept suggestion 8
Suggestion 9
>>> if 99 in all : 
...     print("99")
... 
>>> 
>>> for i in all:
...     print(i)
... 
1
2
3
4
5
11
22
33
44
55

>>> len(all) # length of tuple
10

>>> types.count(2) # count of 2 in tuple
1

>>> types.index(2) # index of 2 in tuple
1

>>> types.index(99) # index of 99 in tuple
Traceback (most recent call last):
  File "<python-input-63>", line 1, in <module>
    types.index(99) # index of 99 in tuple
ValueError: tuple.index(x): x not in tuple

Accept suggestion 9
Suggestion 10
>>> if 12 in all : 
...     print("11")
... 
>>> 
>>> len(all)
10
>>> types.count(1)
1
>>> types.index(3)
2
>>> types.index(5, 0, 4)
4
>>> types.index(5, 0, 5)
Traceback (most recent call last):
  File "<python-input-60>", line 1, in <module>
    types.index(5, 0, 5)
TypeError: tuple.index(x[, start[, end]]) argument 2 must be int, not tuple
>>>


## ------------------------------------------------------------

Here’s a detailed breakdown of **Python Tuple** theory along with **common problems and examples** to help you master it, Gayatri 📘

---

## 📚 **Tuple in Python – Complete Theory**

### ✅ **What is a Tuple?**
- A **tuple** is a built-in **immutable**, **ordered** data type.
- It allows **duplicates** and stores **multiple items** in a **single variable**.

### 🔹 **Tuple Syntax:**
```python
my_tuple = (1, 2, 3)
```

### 🔹 **Key Features:**
| Feature       | Tuple                             |
|---------------|-----------------------------------|
| Mutable       | ❌ Immutable (cannot be changed)  |
| Ordered       | ✅ Yes                            |
| Allows Duplicates | ✅ Yes                        |
| Indexing      | ✅ Supports indexing/slicing      |
| Hashable      | ✅ Can be used as dictionary keys |

---

## 🧪 **Tuple Examples**

### 📌 Create a Tuple
```python
t = (10, 20, 30)
print(t[1])  # Output: 20
```

### 📌 Tuple with Mixed Data Types
```python
person = ('Gayatri', 17, 'Nashik')
```

### 📌 Singleton Tuple (Important!)
```python
x = (5,)  # Must include comma!
```

### 📌 Nested Tuple
```python
nested = (1, (2, 3), [4, 5])
```

### 📌 Slicing a Tuple
```python
t = (10, 20, 30, 40)
print(t[1:3])  # Output: (20, 30)
```

---

## 🔧 **Tuple Methods**

| Method        | Description                    |
|---------------|--------------------------------|
| `count(x)`    | Returns the number of times `x` appears |
| `index(x)`    | Returns the first index of `x` |

Example:
```python
t = (1, 2, 3, 2)
print(t.count(2))  # Output: 2
print(t.index(3))  # Output: 2
```

---

## ❗ Why Use Tuple Instead of List?
- More memory efficient ✅  
- Safe from accidental changes ✅  
- Can be used as dictionary keys ✅

---

## ⚠️ Common Mistakes & Problems

### ❌ Modifying Tuple
```python
t = (1, 2, 3)
t[0] = 10  # ❌ Error: 'tuple' object does not support item assignment
```

### ✅ Solution: Convert to List
```python
t = (1, 2, 3)
lst = list(t)
lst[0] = 10
t = tuple(lst)
print(t)  # (10, 2, 3)
```

---

## 🎯 Tuple Interview Problem Example

### 🔸 **Problem: Swap Two Values Using Tuple**
```python
a = 5
b = 10
a, b = b, a
print(a, b)  # 10 5
```

### 🔸 **Problem: Return Multiple Values**
```python
def get_status():
    return ("Success", 200)

status, code = get_status()
print(status, code)
```

---

Would you like this as a **PDF** too?  
And want me to prepare a **quiz or practice problems** for Tuple? 😊