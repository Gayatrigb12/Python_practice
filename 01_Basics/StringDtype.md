# Strings 



Example 

>>> chai = "Masala Chai"
>>> first_ch = chai[0]  # for first char in string (here we use [] becasue string is treated as list)
>>> print(first_ch)
M

# slice

>>> slice_chai = chai[0 : 6]
>>> slice_chai
'Masala'
>>> print(slice_chai)
Masala

>>> num_list = "0123456789"
>>> num_list[:]
'0123456789'
>>> num_list[3:]
'3456789'
>>> num_list[:7]
'0123456'
>>> num_list[0:7:2]
'0246'

# hopping 
>>> num_list[0:7:2]
'0246'

>>> num_list[0::2]
'02468'
>>> num_list[0::3]
'0369'


# upper lower 
>>> chai = 'Masala Chai'
>>> chai
'Masala Chai'
>>> print(chai.lower())
masala chai
>>> print(chai.upper())
MASALA CHAI

# strip

>>> demo = "    HELLO     "
>>> demo
'    HELLO     '
>>> print(demo.strip())
HELLO

# replace 
chai = "ginger tea"
>>> chai
'ginger tea'
>>> print(chai.replace("ginger" , "lemon"))
lemon tea


# split 

 chai ="abc, xyz, lmn, opq"
>>> chai
'abc, xyz, lmn, opq'
>>> print(chai.split())
['abc,', 'xyz,', 'lmn,', 'opq']
>>> print(chai.split(", "))
['abc', 'xyz', 'lmn', 'opq']


# find 

chai = "hello world"
>>> print(chai.find("world"))
6 # it give from which index its started
>>> print(chai.find("World"))
-1 # it indicate vlue not found 

print(chai.find("o"))
4 # it will give first occurence of the string 
>>> print(chai.rfind("o"))
7 # it will give last occurence of the string 
print(chai.find("o", 5)) # it give from which index its started
4 # it start searching from index 5 
>>> print(chai.find("o", 6)) # it give from which index its started
7 # it start searching from index 6
>>> 
# count
>>> print(chai.count("l"))
3
>>> print(chai.count("p"))
0
>>> print(chai.count("l", 0, 5)) # it count between the given range 
2


# join 
>>> chai = ["hello", "world"]
>>> print(" ".join(chai))
hello world
>>> print(", ".join(chai))
hello, world

print(" ".join("hello world"))
h e l l o   w o r l d


chai = ['hello' , 'java' , 'python']
>>> chai
['hello', 'java', 'python']
print("".join(chai))
hellojavapython
>>> print(" ".join(chai))
hello java python
>>> print("-".join(chai))
hello-java-python
# title 
>>> chai = "hello world"
>>> print(chai.title())
Hello World # all first letter is capitalized 

# string concatenation 
>>> chai1 = "hello"
>>> chai2 = "world"
>>> print(chai1 + chai2)
helloworld
>>> print(chai1 + " " + chai2)
hello world

# format (use to add valriable)
>>> chai_type = "masala"
>>> quantity = 2
>>> order ="i ordered {}  cups of {} chai"
>>> print(order)
i ordered {}  cups of {} chai
>>> print(order.format(quantity,chai_type))
i ordered 2  cups of masala chai

# loop 
hai = "hello world"
>>> chai
'hello world'
>>> for letter in chai:
...     print(letter)
...     
h
e
l
l
o
 
w
o
r
l
d


# condition (chai = "He said. "Masala chai is good"")

chai = "He said. \"Masala chai is good\""
>>> chai
'He said. "Masala chai is good"'

# r string (row string )
>>> x = "abc\nxyz"
>>> print(x)
abc
xyz
>>> x = r"abc\nxyz"
>>> print(x)
abc\nxyz


ex  2 

>>> path = r"D:\PYTHON\xyz"
>>> print(path)
D:\PYTHON\xyz
>>> path = "D:\PYTHON\xyz"
  File "<python-input-61>", line 1
    path = "D:\PYTHON\xyz"
           ^^^^^^^^^^^^^^^
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 9-10: truncated \xXX escape
# -------------------------------------------------------------------------------------------------------------
# how many ways we can define string 

In Python, strings can be defined in multiple ways using different syntax. Here are the **7 main ways** to define a string:

---

## **1️⃣ Single Quotes (`'...'`)**
- Used for defining simple strings.  
```python
s1 = 'Hello, Python!'
print(s1)  # Output: Hello, Python!
```

---

## **2️⃣ Double Quotes (`"..."`)**
- Works the same as single quotes.  
```python
s2 = "Hello, World!"
print(s2)  # Output: Hello, World!
```
🔹 **Why use double quotes?** When the string itself contains a single quote:
```python
s3 = "It's a sunny day!"
print(s3)  # Output: It's a sunny day!
```

---

## **3️⃣ Triple Quotes (`'''...'''` or `"""..."""`)**
- Used for **multiline strings** and docstrings.  
```python
s4 = '''This is 
a multiline 
string.'''
print(s4)
```
```python
s5 = """This is also 
a multiline string."""
print(s5)
```

---

## **4️⃣ String Using `str()` Constructor**
- Converts other data types to a string.
```python
s6 = str(100)  # Converts integer to string
print(s6)  # Output: '100'
```

---

## **5️⃣ Using `repr()` for String Representation**
- `repr()` gives an unambiguous representation (useful for debugging).
```python
s7 = repr("Hello\nWorld")
print(s7)  # Output: "'Hello\\nWorld'"
```

---

## **6️⃣ Using `bytes.decode()` to Create a String**
- Converts a byte object to a string.
```python
s8 = bytes("Python", "utf-8").decode("utf-8")
print(s8)  # Output: Python
```

---

## **7️⃣ Using `f-strings` (Formatted Strings)**
- Introduced in Python 3.6, used for dynamic string formatting.
```python
name = "Alice"
age = 25
s9 = f"My name is {name} and I am {age} years old."
print(s9)  # Output: My name is Alice and I am 25 years old.
```

---

## ✅ **Summary Table**
| Method | Example | Use Case |
|--------|---------|----------|
| Single Quotes (`'...'`) | `'Hello'` | Simple strings |
| Double Quotes (`"..."`) | `"Hello"` | Strings containing `'` |
| Triple Quotes (`'''...'''` or `"""..."""`) | `'''Hello'''` | Multiline strings |
| `str()` Constructor | `str(123)` | Convert data types to string |
| `repr()` Function | `repr("Hello")` | Debugging, unambiguous representation |
| `bytes.decode()` | `b'Python'.decode()` | Converting bytes to string |
| f-strings (`f"..."`) | `f"My name is {name}"` | String formatting |






# DIFFERENCES 


# **Different Ways to Define Strings in Python & Their Differences**  

In Python, **strings** can be defined in multiple ways, each with specific use cases and behaviors. Below is a detailed comparison of all the ways to define strings.

---

## **1️⃣ Single Quotes (`' '`)**
- Used for defining **simple, single-line** strings.
- Strings must be on **one line**.

### **Example:**
```python
str1 = 'Hello, Python!'
print(str1)  # Output: Hello, Python!
```

### ✅ **Pros:**
✔️ Short and simple.  
✔️ Good for defining small strings.  

### ❌ **Cons:**
❌ Can't include **single quotes (`'`)** inside without escaping them.  

#### **Example of Escape Issue:**
```python
str2 = 'It's a beautiful day'  # ❌ Error: Unexpected apostrophe in "It's"
```

#### **Solution (Escaping `'` using `\`):**
```python
str2 = 'It\'s a beautiful day'  # ✅ Correct way
print(str2)  # Output: It's a beautiful day
```

---

## **2️⃣ Double Quotes (`" "`)**
- Works **similarly** to single quotes.
- Preferred when the string contains **single quotes (`'`)**, making escape characters unnecessary.

### **Example:**
```python
str3 = "It's a beautiful day"  # No escape needed
print(str3)  # Output: It's a beautiful day
```

### ✅ **Pros:**
✔️ Can include **single quotes** (`'`) inside without escaping.  

### ❌ **Cons:**
❌ Must use escaping (`\"`) if the string contains **double quotes (`"`)**.

#### **Example of Escape Issue:**
```python
str4 = "She said, "Hello!""  # ❌ SyntaxError
```

#### **Solution (Escaping `"` using `\`):**
```python
str4 = "She said, \"Hello!\""  # ✅ Correct way
print(str4)  # Output: She said, "Hello!"
```

---

## **3️⃣ Triple Single Quotes (`''' '''`)**
- Used for **multi-line strings**.
- Preserves formatting (new lines, spaces, etc.).
- Often used for **docstrings** (documentation).

### **Example:**
```python
str5 = '''This is
a multi-line
string.'''
print(str5)
```
#### **Output:**
```
This is
a multi-line
string.
```

### ✅ **Pros:**
✔️ Can contain both **single (`'`) and double (`"`) quotes** without escaping.  
✔️ Preserves **multi-line formatting**.  

### ❌ **Cons:**
❌ Not ideal for short, single-line strings (wastes memory).  

---

## **4️⃣ Triple Double Quotes (`""" """`)**
- Works the same as triple single quotes.
- **Commonly used for docstrings** in functions, classes, and modules.

### **Example (Docstring in Function):**
```python
def greet():
    """This function prints a greeting message."""
    print("Hello!")

print(greet.__doc__)  # Accessing the docstring
```

#### **Output:**
```
This function prints a greeting message.
```

### ✅ **Pros:**
✔️ Best for **writing documentation** (docstrings).  
✔️ Multi-line support, **preserves formatting**.  

### ❌ **Cons:**
❌ Like `''' '''`, **not memory efficient** for short strings.  

---

## **5️⃣ Raw Strings (`r'...'` or `r"..."`)**
- **Prevents escape sequences (`\n`, `\t`, `\b`, etc.)** from being processed.
- Useful for **regular expressions (regex), file paths, etc.**.

### **Example:**
```python
str6 = r'C:\Users\new_folder\file.txt'  
print(str6)  
```
#### **Output:**
```
C:\Users\new_folder\file.txt
```

🔹 Without `r`, `\n` would be interpreted as a **new line**.  

### ✅ **Pros:**
✔️ Useful for **regex, file paths, and Windows directories**.  

### ❌ **Cons:**
❌ Cannot end with an **odd number of backslashes (`\`)**.

#### **Example of Issue:**
```python
str7 = r'C:\Users\new_folder\'  # ❌ SyntaxError
```

#### **Solution (Adding Double `\\`):**
```python
str7 = r'C:\Users\new_folder\\'  # ✅ Correct way
```

---

## **6️⃣ Byte Strings (`b'...'`)**
- Used for handling **binary data** (e.g., images, files, network communication).
- **Prefix `b`** before a string converts it into a **bytes object**.

### **Example:**
```python
byte_str = b'Hello'
print(byte_str)  # Output: b'Hello'
print(type(byte_str))  # Output: <class 'bytes'>
```

### ✅ **Pros:**
✔️ Used for **handling raw binary data**.  
✔️ More **memory-efficient** than Unicode strings.  

### ❌ **Cons:**
❌ Cannot contain **non-ASCII characters** directly.  

#### **Example of Issue:**
```python
byte_str = b'हेलो'  # ❌ UnicodeEncodeError
```

#### **Solution (Encoding `utf-8`):**
```python
byte_str = 'हेलो'.encode('utf-8')  # ✅ Correct way
```

---

## **7️⃣ Formatted Strings (`f'...'` or `f"..."`) – f-strings**
- Introduced in Python 3.6+.
- Allows embedding **variables and expressions** inside `{}`.

### **Example:**
```python
name = "Alice"
age = 25

str8 = f"My name is {name} and I am {age} years old."
print(str8)  
```
#### **Output:**
```
My name is Alice and I am 25 years old.
```

### ✅ **Pros:**
✔️ Best for **string formatting**.  
✔️ Supports **expressions** inside `{}`.

#### **Example with Expressions:**
```python
x = 5
y = 10
print(f"Sum of {x} and {y} is {x + y}")  # Output: Sum of 5 and 10 is 15
```

### ❌ **Cons:**
❌ **Requires Python 3.6+**.  

---

# **🔍 Comparison Table: All Ways to Define Strings**
| String Type | Syntax | Multi-line? | Escape Needed? | Use Case |
|------------|--------|------------|---------------|----------|
| **Single Quotes** | `'Hello'` | ❌ No | ✅ Yes (`It\'s`) | Short strings |
| **Double Quotes** | `"Hello"` | ❌ No | ✅ Yes (`"She said, \"Hello\"."`) | Short strings with `'` |
| **Triple Single Quotes** | `'''Hello'''` | ✅ Yes | ❌ No | Multi-line strings, docstrings |
| **Triple Double Quotes** | `"""Hello"""` | ✅ Yes | ❌ No | Multi-line, documentation |
| **Raw Strings** | `r'Hello\n'` | ❌ No | ❌ No | File paths, regex |
| **Byte Strings** | `b'Hello'` | ❌ No | ✅ Yes | Binary data (files, networking) |
| **f-Strings** | `f'Hello {name}'` | ❌ No | ❌ No | String formatting |

---

# **🎯 Conclusion**
- **Use `' '` or `" "` for short, simple strings.**
- **Use `''' '''` or `""" """` for multi-line strings.**
- **Use `r' '` for raw strings (file paths, regex).**
- **Use `b' '` for byte strings (binary data).**
- **Use `f' '` for string formatting (modern & efficient).**

Each method has its advantages and should be **chosen based on the specific use case**. 🚀