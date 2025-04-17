# 01 Decorators 

In Python, **decorators** are a powerful tool that allow you to modify or enhance the behavior of functions or classes without changing their actual code.

### 🔹 Basic Idea:
A **decorator** is a function that takes another function as an argument, adds some functionality to it, and returns a new function.

---

### 🔧 Syntax:

```python
@decorator_name
def my_function():
    pass
```

This is just shorthand for:

```python
def my_function():
    pass

my_function = decorator_name(my_function)
```

---

### ✅ Example 1: A simple decorator

```python
def my_decorator(func):
    def wrapper():
        print("Something before the function runs")
        func()
        print("Something after the function runs")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
```

**Output:**
```
Something before the function runs
Hello!
Something after the function runs
```

---

### ✅ Example 2: Decorator with arguments

```python
def greet_decorator(func):
    def wrapper(name):
        print("Preparing to greet...")
        func(name)
        print("Greeted successfully.")
    return wrapper

@greet_decorator
def greet(name):
    print(f"Hello, {name}!")

greet("Gayatri")
```

**Output:**
```
Preparing to greet...
Hello, Gayatri!
Greeted successfully.
```

---

### 📌 Use Cases:
- Logging
- Access control (authentication)
- Caching
- Timing functions
- Input validation

---

# 02 walrusOperator

Ah yes — the **Walrus Operator** (`:=`) is a cool feature in Python introduced in **Python 3.8**.

---

### 🦭 What is the Walrus Operator?

The walrus operator `:=` is used to **assign a value to a variable as part of an expression** — especially useful in places where you couldn’t use `=` before.

It’s called the **walrus operator** because it kind of looks like a walrus face: `:=`

---

### 🔍 Syntax:

```python
variable := expression
```

This means:  
> Evaluate `expression`, assign it to `variable`, and also return its value.

---

### ✅ Example 1: Without Walrus

```python
name = input("Enter your name: ")
while name != "":
    print(f"Hello, {name}!")
    name = input("Enter your name: ")
```

### ✅ With Walrus:

```python
while (name := input("Enter your name: ")) != "":
    print(f"Hello, {name}!")
```

➡️ Cleaner and shorter code!

---

### ✅ Example 2: In list comprehensions

```python
# Get only words with length >= 5 and store their lengths
words = ["hello", "to", "python", "code"]
lengths = [length for word in words if (length := len(word)) >= 5]

print(lengths)  # Output: [5, 6, 4]
```

---

### 🔒 Note:
- You can’t use it as a **statement** on its own in older Python versions (pre-3.8).
- It’s useful for **reducing code repetition**, especially in `while` loops and comprehensions.

---

### 📌 Summary:

| Symbol | Name | Use |
|--------|------|-----|
| `:=` | Walrus Operator | Assign + return in one line |

Want me to give a fun mini-exercise using the walrus operator?


Great question! Understanding the difference between `try...else` and `try...finally` is super useful for writing clean and safe Python code.

---

## 🔍 `try...else` vs `try...finally`

### ✅ 1. `try...else`

- The `else` block runs **only if no exception** is raised in the `try` block.
- Use it for code that should **only run when `try` is successful**.

```python
try:
    x = int(input("Enter a number: "))
except ValueError:
    print("That's not a number!")
else:
    print(f"You entered {x} successfully.")
```

🟢 If input is valid, `else` runs.  
🔴 If an exception occurs, `except` runs, and `else` is skipped.

---

### ✅ 2. `try...finally`

- The `finally` block **always runs**, no matter what:
  - Exception or no exception
  - With or without `return`, `break`, `continue`

```python
try:
    x = 1 / int(input("Enter a number: "))
except ZeroDivisionError:
    print("Cannot divide by zero!")
finally:
    print("This runs no matter what (cleanup, close file, etc).")
```

✅ Useful for **cleanup tasks** — like closing files, releasing resources, etc.

---

### 💡 Summary Table:

| Structure        | When it Runs                          | Purpose                         |
|------------------|----------------------------------------|----------------------------------|
| `try...else`     | Only if `try` succeeds (no exception) | Safe extra logic after try      |
| `try...finally`  | Always, even if exception happens     | Cleanup tasks, guarantee execution |

---

### 🧠 Tip:

You can even **combine all**:

```python
try:
    f = open("test.txt", "r")
    data = f.read()
except FileNotFoundError:
    print("File not found!")
else:
    print("File read successfully.")
finally:
    print("Closing file.")
    f.close()
```
