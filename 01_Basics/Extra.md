# what is difference between repr , str , print 

>>> repr('cha')
"'cha'"   
>>> str('cha')
'cha'
>>> print('cha')
cha

example 

>>> repr(int(2.0 ))
'2'

ans 

In Python, `repr()`, `str()`, and `print()` are used for string representations of objects, but they serve different purposes.  

---

## 🔹 `repr()`
- **Goal:** Provides an **official** string representation of an object that can be used to recreate it.  
- **Intended for:** Developers (debugging, logging).  
- **Output:** Usually more detailed and unambiguous.  
- **Best Practice:** `repr(obj) → eval(repr(obj))` should recreate the object (if possible).  

✅ **Example:**  
```python
x = "Hello"
print(repr(x))  # Output: "'Hello'"  (Quotes included)
```
```python
import datetime
now = datetime.datetime(2025, 4, 3, 12, 30)
print(repr(now))  
# Output: "datetime.datetime(2025, 4, 3, 12, 30)"
```

---

## 🔹 `str()`
- **Goal:** Provides a **readable** and user-friendly string representation.  
- **Intended for:** End users.  
- **Output:** More concise and human-readable.  

✅ **Example:**  
```python
print(str(x))  # Output: Hello  (No quotes)
```
```python
print(str(now))  
# Output: "2025-04-03 12:30:00"
```

---

## 🔹 `print()`
- **Goal:** Displays a value on the console (calls `str()` internally).  
- **Intended for:** Displaying output to users.  
- **Output:** Does not return a string, just prints it.  

✅ **Example:**  
```python
print(now)  
# Output: 2025-04-03 12:30:00  (Same as str())
```

---

## 🔥 Key Differences

| Function  | Purpose | Output Type | Example Output for `datetime.datetime(2025, 4, 3, 12, 30)` |
|-----------|---------|-------------|-----------------------------------|
| `repr()`  | Debugging (detailed) | **Unambiguous, code-like** | `"datetime.datetime(2025, 4, 3, 12, 30)"` |
| `str()`   | User-friendly | **Readable** | `"2025-04-03 12:30:00"` |
| `print()` | Displays output | **None (prints str(obj))** | `2025-04-03 12:30:00` |

---

## ✅ Custom Class Example
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person('{self.name}', {self.age})"

    def __str__(self):
        return f"{self.name} ({self.age} years old)"

p = Person("Alice", 30)

print(repr(p))  # Output: "Person('Alice', 30)"
print(str(p))   # Output: "Alice (30 years old)"
print(p)        # Output: "Alice (30 years old)" (calls str() internally)
```

**👉 Summary:**  
- `repr()` → For debugging, detailed representation.  
- `str()` → For users, readable representation.  
- `print()` → Calls `str()`, just displays output. 🚀