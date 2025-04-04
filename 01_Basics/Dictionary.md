# Dictionary 

EXAMPLES 

>>> dict = {1:"one" , 2:"two" , 3:"three"}
>>> dict
{1: 'one', 2: 'two', 3: 'three'}
>>> for li in dict:
...     print(li)
...     
1
2
3


>>> for key , value in dict.items():
...     print(key , value)
...     
1 one
2 two
3 three

>>> for li in dict:
...     print(li , dict[li])
... 
1 one
2 two
3 three
>>> 

# nested dict 

>>> tea_shop = {
... "chai": {"masala" : "spicy" , "ginger" : "zesty"} ,
... "tea": {"green": "mild" , "black" :"strong"}
... }
>>> tea_shop
{'chai': {'masala': 'spicy', 'ginger': 'zesty'}, 'tea': {'green': 'mild', 'black': 'strong'}}

>>> tea_shop["chai"]
{'masala': 'spicy', 'ginger': 'zesty'}

>>> tea_shop["chai"]["ginger"]
'zesty'

>>> square = {x:x**2 for x in range(10)}
>>> square
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}  
>>> 

>>> square.clear()
>>> square
{}



# create dictionary by fromkey()

>>> keys = [1,2,3,4]
>>> keys
[1, 2, 3, 4]
>>> default = "delicious"
>>> new_dict = dict.fromkeys(keys, default)
>>> 
>>> new_dict
{1: 'delicious', 2: 'delicious', 3: 'delicious', 4: 'delicious'}
>>> 


>>> new_dict = dict.fromkeys(keys, keys)
>>> new_dict
{1: [1, 2, 3, 4], 2: [1, 2, 3, 4], 3: [1, 2, 3, 4], 4: [1, 2, 3, 4]}
>>> 



# -------------------------------------------

Awesome! Let's dive into **Dictionaries in Python** with complete theory and examples to help you understand everything clearly.

---

## 🧠 **Python Dictionary – Theory + Examples**

---

### 📘 **1. What is a Dictionary?**

A **dictionary** in Python is an **unordered**, **mutable**, and **indexed** collection of **key-value pairs**. It is used to store data values like a map or lookup table.

> ✅ **Key features of dictionaries:**
- Each item is a pair: `key: value`
- Keys must be **unique** and **immutable** (like strings, numbers, tuples)
- Values can be of any type and can repeat
- Dictionaries are defined using **curly braces `{}`**

---

### 📘 **2. Creating a Dictionary**

```python
# Empty dictionary
empty_dict = {}

# Dictionary with data
student = {
    'name': 'Rahul',
    'age': 18,
    'grade': 'A',
    'marks': [85, 90, 78]
}

print(student)
```

---

### 📘 **3. Accessing Values**

You can access values using the **key**:

```python
print(student['name'])    # Rahul
print(student['marks'])   # [85, 90, 78]
```

You can also use `.get()` method (it doesn’t throw error if the key doesn’t exist):

```python
print(student.get('age'))         # 18
print(student.get('address'))     # None
```

---

### 📘 **4. Modifying Dictionary**

```python
student['grade'] = 'A+'
student['email'] = 'rahul@example.com'  # adding new key-value pair

print(student)
```

---

### 📘 **5. Removing Elements**

| Method          | Description                              |
|-----------------|------------------------------------------|
| `pop(key)`      | Removes and returns value of the key     |
| `popitem()`     | Removes and returns the **last** item    |
| `del dict[key]` | Deletes specific key                     |
| `clear()`       | Removes all elements                     |

```python
student.pop('age')
del student['grade']
student.clear()   # Now it's an empty dict
```

---

### 📘 **6. Dictionary Methods**

| Method             | Description                              |
|--------------------|------------------------------------------|
| `keys()`           | Returns all keys                         |
| `values()`         | Returns all values                       |
| `items()`          | Returns list of key-value pairs (tuples) |
| `update(dict2)`    | Merges `dict2` into the dictionary       |
| `copy()`           | Returns a shallow copy                   |

```python
info = {'name': 'Amit', 'city': 'Nashik'}

print(info.keys())     # dict_keys(['name', 'city'])
print(info.values())   # dict_values(['Amit', 'Nashik'])

for key, value in info.items():
    print(key, value)
```

---

### 📘 **7. Looping Through a Dictionary**

```python
for key in student:
    print(key, student[key])

# or

for key, value in student.items():
    print(f"{key}: {value}")
```

---

### 📘 **8. Nested Dictionary**

A dictionary inside another dictionary:

```python
students = {
    '101': {'name': 'Ravi', 'grade': 'A'},
    '102': {'name': 'Sneha', 'grade': 'B'}
}

print(students['101']['name'])  # Ravi
```

---

### 📘 **9. Dictionary Comprehension**

Short and powerful way to create dictionaries:

```python
squares = {x: x*x for x in range(1, 6)}
print(squares)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

---

### 🆚 **List vs Dictionary**

| Feature       | List                      | Dictionary                     |
|---------------|---------------------------|--------------------------------|
| Structure     | Ordered collection        | Unordered key-value pairs      |
| Access        | By index                  | By key                         |
| Mutable       | Yes                       | Yes                            |
| Syntax        | `[1, 2, 3]`               | `{'a': 1, 'b': 2}`             |
| Use Case      | Sequential data           | Labeled data (like records)    |

---

### 🧪 **Mini Exercise:**

Create a dictionary of a book with the following keys:
- `title`, `author`, `year`, `price`

Then:
1. Add a new key: `'genre'`
2. Update the price
3. Print all key-value pairs

Want me to show the solution too?

---
\

