# SET  (define in {})

 its comes under numbers 
 its declaration same as Dictionary but diffrence is 
 - Dict have key value pair 
 - set do not have that 
 same as math set 

-- you can do union , intersection , subset , superset etc  operation same as set in math 
Example 

# Intersection (use & (AND sign))
>>> set1 = { 1 , 2 , 3 , 4 }
>>> set1 & { 1 , 3 }
{1, 3}
>>> set1 & { 1 , 3 , 5}
{1, 3}

# Union (use | (OR sign))

>>> set1 | { 1 , 3 , 5}
{1, 2, 3, 4, 5}

# Difference ( - (SUBSTRACT sign ))
>>> set1 - { 1 , 3 , 5}
{2, 4}


# Empty set ( its define as set())

its uses set() because { } this indicate dict
>>> set1 - { 1, 2 , 3 , 4 }
set() #its uses set() because { } this indicate dict
>>> type({})
<class 'dict'>

# =========================================================================================================

# SET 

# **Python `set` - Complete Guide**  
A **set** in Python is an **unordered**, **mutable**, and **unindexed** collection that only stores **unique** elements. Sets are useful for mathematical operations like union, intersection, and difference.

---

## **1️⃣ Creating a Set**  
You can create a set using `{}` or the `set()` constructor.

```python
# Using curly braces
my_set = {1, 2, 3, 4}
print(my_set)  # Output: {1, 2, 3, 4}

# Using set() function
my_set2 = set([4, 5, 6, 6, 7])
print(my_set2)  # Output: {4, 5, 6, 7} (removes duplicates)
```

🔹 **Note:**  
- Duplicates are **automatically removed**.
- Sets are **unordered**, meaning elements have **no fixed position**.

---

## **2️⃣ Adding Elements to a Set**
Use `add()` for a single element and `update()` for multiple elements.

```python
my_set = {1, 2}
my_set.add(3)  # Adds a single element
print(my_set)  # Output: {1, 2, 3}

my_set.update([4, 5, 6])  # Adds multiple elements
print(my_set)  # Output: {1, 2, 3, 4, 5, 6}
```

---

## **3️⃣ Removing Elements from a Set**
You can remove elements using `remove()`, `discard()`, or `pop()`.

```python
# Using remove() (Raises an error if the element is missing)
my_set = {1, 2, 3}
my_set.remove(2)
print(my_set)  # Output: {1, 3}

# Using discard() (Does NOT raise an error if the element is missing)
my_set.discard(5)  # No error, even though 5 is not in the set

# Using pop() (Removes a random element)
removed_item = my_set.pop()
print(removed_item)  # Random element removed
print(my_set)  # Remaining elements
```

🔹 **Difference:**  
- `remove(x)` → Throws an error if `x` is not found.  
- `discard(x)` → Does nothing if `x` is not found.  
- `pop()` → Removes and returns a **random** element.  

---

## **4️⃣ Checking Membership**
You can check if an element exists in a set using the `in` keyword.

```python
my_set = {1, 2, 3, 4}
print(2 in my_set)  # Output: True
print(5 in my_set)  # Output: False
```

---

## **5️⃣ Set Operations**
Python sets support mathematical operations like **union, intersection, difference, and symmetric difference**.

### **🔹 Union (`|` or `union()`)**  
Combines all elements from both sets.

```python
A = {1, 2, 3}
B = {3, 4, 5}
print(A | B)  # Output: {1, 2, 3, 4, 5}
print(A.union(B))  # Same as above
```

### **🔹 Intersection (`&` or `intersection()`)**  
Finds common elements.

```python
print(A & B)  # Output: {3}
print(A.intersection(B))  # Same as above
```

### **🔹 Difference (`-` or `difference()`)**  
Elements in `A` but not in `B`.

```python
print(A - B)  # Output: {1, 2}
print(A.difference(B))  # Same as above
```

### **🔹 Symmetric Difference (`^` or `symmetric_difference()`)**  
Elements in either `A` or `B`, but not in both.

```python
print(A ^ B)  # Output: {1, 2, 4, 5}
print(A.symmetric_difference(B))  # Same as above
```

---

## **6️⃣ Set Methods Summary**
| Method | Description | Example |
|--------|-------------|---------|
| `add(x)` | Adds an element to the set | `s.add(5)` |
| `update(iterable)` | Adds multiple elements | `s.update([3, 4, 5])` |
| `remove(x)` | Removes `x`, raises an error if not found | `s.remove(2)` |
| `discard(x)` | Removes `x`, does nothing if not found | `s.discard(2)` |
| `pop()` | Removes and returns a random element | `s.pop()` |
| `clear()` | Removes all elements | `s.clear()` |
| `union(set2)` | Combines elements from both sets | `s1.union(s2)` |
| `intersection(set2)` | Finds common elements | `s1.intersection(s2)` |
| `difference(set2)` | Finds elements in `s1` but not in `s2` | `s1.difference(s2)` |
| `symmetric_difference(set2)` | Finds elements in `s1` or `s2`, but not both | `s1.symmetric_difference(s2)` |

---

## **7️⃣ Frozen Set (`frozenset`)**
A **frozen set** is an **immutable** version of a set. Once created, its elements **cannot be changed**.

```python
fs = frozenset([1, 2, 3])
print(fs)  # Output: frozenset({1, 2, 3})

# fs.add(4)  # ❌ Error: 'frozenset' object has no attribute 'add'
```
🔹 **Use case:** Frozen sets are useful as dictionary keys or for storing immutable collections.

---

## **8️⃣ Set Comprehensions**
Like list comprehensions, Python supports **set comprehensions**.

```python
squared_set = {x ** 2 for x in range(5)}
print(squared_set)  # Output: {0, 1, 4, 9, 16}
```

---

## **✅ Summary**
| Feature | Description |
|---------|-------------|
| **Mutable?** | ✅ Yes (Can add/remove elements) |
| **Duplicates?** | ❌ No (Only unique values) |
| **Ordered?** | ❌ No (Unordered collection) |
| **Indexed?** | ❌ No (Cannot access elements by index) |
| **Common Uses** | Removing duplicates, mathematical operations, membership tests |

Sets in Python are **powerful and efficient**, especially for handling unique items and mathematical operations. 🚀