# Scope or namespace in python 

Sure! Let's dive deeper into **local** and **global scope** in Python — these are the most commonly used and most important to understand when you're starting with functions and variables.

---

## 🔸 Local Scope in Python

### ✅ Definition:
A variable declared **inside a function** is said to be in the **local scope** of that function. It **can only be accessed inside that function**.

### 🔍 Example:
```python
def greet():
    message = "Hello from inside!"  # local variable
    print(message)

greet()
# print(message)  # ❌ Error: 'message' is not defined outside the function
```

### ⚠️ Key Point:
- Local variables are **created when the function is called**.
- They **disappear** when the function ends.

---

## 🔸 Global Scope in Python

### ✅ Definition:
A variable declared **outside all functions or classes** is in the **global scope**. It can be **accessed from anywhere** in the file (including inside functions).

### 🔍 Example:
```python
language = "Python"  # global variable

def show_language():
    print("I'm learning", language)

show_language()  # Works fine because language is global
```

---

## ⚠️ Modifying Global Variables Inside Functions

By default, if you try to **change** a global variable inside a function, Python creates a **new local variable** with the same name instead. To actually modify the global variable, you need to use the **`global` keyword**.

### 🔍 Example **without** `global`:
```python
count = 0

def increment():
    count = count + 1  # ❌ Error: UnboundLocalError
    print(count)

# increment()  # This will raise an error
```

### ✅ Example **with** `global`:
```python
count = 0

def increment():
    global count
    count = count + 1
    print(count)

increment()  # 1
increment()  # 2
```

---

## 🧠 Summary Table

| Feature         | Local Scope                       | Global Scope                      |
|----------------|------------------------------------|-----------------------------------|
| Defined in      | Inside a function                 | Outside all functions             |
| Accessed where  | Only within the function          | Anywhere in the code              |
| Lifetime        | During the function call          | Throughout the program's runtime  |
| Modified inside function? | Needs `nonlocal` or re-declaration | Needs `global` keyword           |

---

## 👀 Tip:
- **Use local variables** when possible — it's safer and cleaner.
- Use **global variables** only when absolutely needed.

Would you like a visual diagram or real-world analogy for this?