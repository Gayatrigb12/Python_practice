# boolean also comes under number data type 
>>> 1 < 2
True
>>> 1 > 2
False
>> 1 != 0
True
>>> 1 == 0
False
>> 1 != 0
True
>>> 1 == 0
False
>>> x < y < z # short hand 
True
>>> x < y and y < z
True


# some cases of Boolean 

>>> True == 1
True
>>> True is 1 
<python-input-110>:1: SyntaxWarning: "is" with 'int' literal. Did you mean "=="?
  True is 1
False
>>> False == 0 
True
>>> False is 0 

-----------------

>>> True + 1
2
<python-input-112>:1: SyntaxWarning: "is" with 'int' literal. Did you mean "=="?
  False is 0
False
>>> false == 0

interview 

>>> 1 == 2 < 3
False

# Number Data Type 

Example 1 

>>> x = 2
>>> y = 3
>>> z = 4
>>> x + y
5
>>> x **  y
8
>>> x -  y
-1
>>> x * y
6
>>> y % 2
1
>>> x + y * z  # not recomondaed in production
14
>>> (x + y )* z # if you want to do above then do it in this way like which is first put that in ()
20
>>> 40 + 20.34
60.34



# type error 
'chai'+1
Traceback (most recent call last):
  File "<python-input-11>", line 1, in <module>
    'chai'+1
    ~~~~~~^~
TypeError: can only concatenate str (not "int") to str

# operator overloading 

>>> 'hello ' + 'world'
'hello world'
>>> 1 + 7
8
>>> 

# convert number datatype 

>>> int(2.09)
2
>>> float(2)
2.0
>>> 



# if we assign dtype before and did comman seperation its convert ast tuple 


>>> x = 2
>>> y = 3
>>> z = 4
>>> x , y , z
(2, 3, 4)

>>> x + 1 , y * 2
(3, 6)


# math 
# math.floor 

 it gives you nearest floor value means (small value than number) towords bottom 
>>> import math 
>>> math.floor(3.5)
3
>>> math.floor(-3.5)
-4
>>> math.floor(3.8)
3
>>> math.floor(4.2)
4


# math.trunc
TRUNCATE
towords zero (nearest value to zero )

>>> math.trunc(2.8)
2
>>> math.trunc(-2.8)
-2

# number precision 

>>> 9999999999999999999999999999999999999999999 + 1
10000000000000000000000000000000000000000000
>>> 9999999999999999999999999999999999999999999 * 2.1
2.1e+43
>>> 2 ** 200
1606938044258990275541962092341162602522202993782792835301376


# dealing with complex no 

>>> 2 + 1j
(2+1j)
>>> 2 + 1j * 3
(2+3j)
>>> (2+3j)* 3
(6+9j)

# octal literal  (start with 0o)
>>> 0o20
16

>>> oct(10)
'0o12'


>>> int( '44' , 8)
36

# hexal (start with 0x)
>>> 0xFF
255

>>> hex(10)
'0xa'

>>> int( '44' , 16)
68
# binary (start with 0b)
>>> 0b1000
8
>>> 0b1001
9

>>> bin(10)
'0b1010'


int( '101' , 2)
5

int( '44' , 2)
Traceback (most recent call last):
  File "<python-input-60>", line 1, in <module>
    int( '44' , 2)
    ~~~^^^^^^^^^^^
ValueError: invalid literal for int() with base 2: '44'

# bitwise operator 

>>> x = 1
>>> x << 2 # left shift by 2 bit 
4

>>> x = 2 
>>> x << 2
8
>>> x =  3
>>> x << 2
12

# random 
# random.random()

import random
>>> random.random()
0.5919438154014742

>>> random.random()
0.13490383629498925
>>>
# random.randint()

>>> random.randint(1, 10)
3
>>> random.randint(1, 10)
8

 # random.choice()
>>> l1= [ 'lemon' , 'masala' , 'ginger' ]
>>> random.choice(l1)
'masala'
>>> random.choice(l1)
'lemon'


# random.shuffle()

>>> random.shuffle(l1)
>>> l1
['lemon', 'ginger', 'masala']

>>> random.shuffle(l1)
>>> l1
['ginger', 'masala', 'lemon']
>>> 

# decimal problem 

>>> 0.1 + 0.1 + 0.4
0.6000000000000001
>>> 0.1 + 0.1 + 0.1
0.30000000000000004
>>> 0.1 + 0.1 + 0.1 - 0.3
5.551115123125783e-17
>>> (0.1 + 0.1 + 0.1) - 0.3
5.551115123125783e-17


# decimal problem solution

>>> from decimal import Decimal
>>> Decimal('0.1') + Decimal('0.1') + Decimal('0.1')
Decimal('0.3')
>>> Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('\0.3')
Decimal('0.0')

# fractions 
>>> from fractions import Fraction
>>> frac = Fraction(2 , 7 )
>>> frac
Fraction(2, 7)

# =========================================================================================================

# NUMBER 

# **Python Number Data Types – Complete Guide**

In Python, **numbers** are one of the fundamental data types used for mathematical computations. Python supports **four main types of numbers**:

1. **int** (Integer)  
2. **float** (Floating-Point)  
3. **complex** (Complex Numbers)  
4. **bool** (Boolean - a subclass of int)  

---

## **1️⃣ Integer (`int`)**
- Used to store **whole numbers** (positive, negative, or zero).  
- **No limit** on size (depends on system memory).  
- **Base conversions**: Binary, Octal, Hexadecimal.

### **Example:**
```python
x = 10         # Positive integer
y = -200       # Negative integer
z = 0          # Zero
print(type(x)) # Output: <class 'int'>

# Binary (0b), Octal (0o), Hexadecimal (0x)
bin_num = 0b1010   # Binary -> Decimal (10)
oct_num = 0o12     # Octal -> Decimal (10)
hex_num = 0xA      # Hexadecimal -> Decimal (10)

print(bin_num, oct_num, hex_num)  # Output: 10 10 10
```

---

## **2️⃣ Floating-Point (`float`)**
- Used to store **decimal numbers**.  
- Python **follows IEEE 754** double-precision floating point standard.  
- Can represent **scientific notation**.

### **Example:**
```python
a = 10.5        # Positive float
b = -20.75      # Negative float
c = 1.5e3       # Scientific notation (1.5 × 10³ = 1500)
d = 2.5e-2      # Scientific notation (2.5 × 10⁻² = 0.025)

print(type(a))  # Output: <class 'float'>
print(c, d)     # Output: 1500.0 0.025
```

🔹 **Note:** Floating-point arithmetic may introduce small precision errors due to binary representation.

---

## **3️⃣ Complex Numbers (`complex`)**
- Used for **mathematical computations** involving imaginary numbers.  
- Written in the form **`a + bj`**, where `a` (real part) and `b` (imaginary part).  
- `j` is used to represent **√(-1) (i.e., i in mathematics).**  

### **Example:**
```python
comp1 = 3 + 4j   # Complex number
comp2 = 2 - 5j

print(type(comp1))  # Output: <class 'complex'>
print(comp1.real)   # Output: 3.0 (Real part)
print(comp1.imag)   # Output: 4.0 (Imaginary part)
```

---

## **4️⃣ Boolean (`bool`)**
- A **subtype of integers (`int`)**.  
- Only two possible values: **`True` (1) and `False` (0)**.  
- Used for **logical conditions**.

### **Example:**
```python
is_active = True
is_logged = False

print(type(is_active))  # Output: <class 'bool'>
print(is_active + 1)    # Output: 2 (True acts as 1)
print(is_logged * 5)    # Output: 0 (False acts as 0)
```

---

## **5️⃣ Type Conversion (`int`, `float`, `complex`)**
You can **convert** between number types using `int()`, `float()`, and `complex()`.

### **Example:**
```python
# Convert float to int
x = int(10.99)  
print(x)  # Output: 10  (removes decimal part)

# Convert int to float
y = float(10)  
print(y)  # Output: 10.0

# Convert int/float to complex
z = complex(3, 4)  
print(z)  # Output: (3+4j)

# Convert string to number
num_str = "123"
print(int(num_str))  # Output: 123
print(float(num_str))  # Output: 123.0
```

🔹 **Note:**  
- `int()` **truncates** the decimal part (does not round).  
- `complex()` always requires two arguments (`real, imag`).  

---

## **6️⃣ Arithmetic Operations on Numbers**
Python supports basic arithmetic operations.

| Operator | Description | Example |
|----------|------------|---------|
| `+` | Addition | `5 + 3 = 8` |
| `-` | Subtraction | `5 - 3 = 2` |
| `*` | Multiplication | `5 * 3 = 15` |
| `/` | Division (float) | `5 / 2 = 2.5` |
| `//` | Floor Division | `5 // 2 = 2` |
| `%` | Modulus (Remainder) | `5 % 2 = 1` |
| `**` | Exponentiation | `2 ** 3 = 8` |

### **Example:**
```python
a = 10
b = 3

print(a + b)   # 13
print(a - b)   # 7
print(a * b)   # 30
print(a / b)   # 3.333
print(a // b)  # 3  (Floor division)
print(a % b)   # 1  (Remainder)
print(a ** b)  # 1000 (Exponentiation)
```

---

## **7️⃣ Using `math` Module for Advanced Operations**
The `math` module provides extra mathematical functions.

### **Example:**
```python
import math

print(math.sqrt(16))   # 4.0 (Square root)
print(math.factorial(5))  # 120 (5!)
print(math.log(10))    # 2.302 (Natural log)
print(math.ceil(3.4))  # 4 (Round up)
print(math.floor(3.9)) # 3 (Round down)
print(math.pi)         # 3.141592653589793
print(math.e)          # 2.718281828459045
```

---

## **8️⃣ Using `random` Module for Random Numbers**
Python's `random` module generates random numbers.

### **Example:**
```python
import random

print(random.randint(1, 10))  # Random integer between 1 and 10
print(random.random())        # Random float between 0 and 1
print(random.uniform(1, 10))  # Random float between 1 and 10
print(random.choice([10, 20, 30]))  # Random choice from a list
```

---

## **9️⃣ Decimal and Fraction Modules**
Python provides **`decimal`** for high-precision floating-point numbers and **`fractions`** for rational numbers.

### **Using `decimal` for Precise Computation**
```python
from decimal import Decimal

x = Decimal("0.1") + Decimal("0.2")
print(x)  # Output: 0.3 (Precise result)
```

### **Using `fractions` for Rational Numbers**
```python
from fractions import Fraction

f1 = Fraction(1, 3)
f2 = Fraction(2, 3)
print(f1 + f2)  # Output: 1
```

---

## ✅ **Summary**
| Data Type | Description | Example |
|-----------|------------|---------|
| `int` | Whole numbers | `10, -5, 0` |
| `float` | Decimal numbers | `3.14, -2.5` |
| `complex` | Numbers with real & imaginary parts | `2 + 3j` |
| `bool` | Boolean values (subtype of int) | `True (1), False (0)` |

Python provides powerful built-in support for numerical data types, making it a great language for **scientific computing, AI, finance, and engineering applications**. 🚀




# ADVANCE NUMBER 

## **Advanced Number Concepts in Python** 🚀  

Python provides **advanced mathematical functionalities** for handling numbers efficiently. This includes working with **big integers, special functions, mathematical constants, bitwise operations, random number generation, and number representation**.

---

# **1️⃣ Big Integers (Arbitrary Precision)**
Python's `int` **automatically supports arbitrary precision**, meaning it can handle **very large numbers** without overflow.

### **Example:**
```python
big_number = 10**100  # 10 raised to the power of 100
print(big_number)  
# Output: 10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
```
🔹 **In other languages like C, Java, integers have a fixed size**, but Python allows **infinite precision** (limited by memory).

---

# **2️⃣ Advanced `math` Module Functions**
The `math` module provides **advanced mathematical operations**.

### **1. Trigonometric Functions** 📐
```python
import math

print(math.sin(math.pi/2))  # 1.0
print(math.cos(math.pi))    # -1.0
print(math.tan(math.pi/4))  # 1.0
print(math.degrees(math.pi))  # 180 (Convert radians to degrees)
print(math.radians(180))    # 3.14159 (Convert degrees to radians)
```

---

### **2. Logarithmic Functions** 🔢
```python
print(math.log(10))       # Natural log (base e)
print(math.log10(100))    # Log base 10
print(math.log2(8))       # Log base 2
```

---

### **3. Factorial & Combinations** 🧩
```python
print(math.factorial(5))  # 5! = 120
print(math.comb(5, 2))    # 5C2 = 10 (Combinations)
print(math.perm(5, 2))    # 5P2 = 20 (Permutations)
```

---

# **3️⃣ Bitwise Operations (Binary Math)**
Python supports bitwise operations that manipulate numbers at the **binary level**.

| Operator | Description | Example |
|----------|------------|---------|
| `&` | Bitwise AND | `5 & 3 → 1` |
| `|` | Bitwise OR | `5 | 3 → 7` |
| `^` | Bitwise XOR | `5 ^ 3 → 6` |
| `<<` | Left Shift | `5 << 1 → 10` |
| `>>` | Right Shift | `5 >> 1 → 2` |

### **Example:**
```python
a = 5  # Binary: 101
b = 3  # Binary: 011

print(a & b)  # Output: 1 (Binary: 001)
print(a | b)  # Output: 7 (Binary: 111)
print(a ^ b)  # Output: 6 (Binary: 110)
print(a << 1) # Output: 10 (Binary: 1010)
print(a >> 1) # Output: 2 (Binary: 10)
```

🔹 **Use Case:** Bitwise operations are used in **cryptography, networking (IP calculations), and performance optimization**.

---

# **4️⃣ Handling Infinity (`inf`) and Not-a-Number (`NaN`)**
Python provides special values for **infinity (`inf`)** and **Not-a-Number (`NaN`)**.

### **Example:**
```python
pos_inf = float('inf')  # Positive Infinity
neg_inf = float('-inf') # Negative Infinity
nan_value = float('nan') # Not a Number

print(pos_inf > 100000000)  # True
print(neg_inf < -100000000) # True
print(math.isnan(nan_value)) # True
```

🔹 **Use Case:** Used in **machine learning, physics, finance**, where calculations may result in undefined or infinite values.

---

# **5️⃣ `decimal` Module (High Precision Computation)**
Python's `float` has **limited precision**, but `decimal.Decimal` provides **arbitrary precision**.

### **Example:**
```python
from decimal import Decimal, getcontext

getcontext().prec = 50  # Set precision to 50 decimal places

a = Decimal('1.1')
b = Decimal('2.2')
print(a + b)  # Output: 3.3000000000000000000000000000000000000000000000000
```
🔹 **Use Case:** Used in **banking, finance, and scientific calculations** where precision is critical.

---

# **6️⃣ `fractions` Module (Rational Numbers)**
The `fractions` module allows working with **exact fractions**.

### **Example:**
```python
from fractions import Fraction

frac1 = Fraction(3, 4)  # 3/4
frac2 = Fraction(1, 2)  # 1/2

print(frac1 + frac2)  # Output: 5/4
print(frac1 * frac2)  # Output: 3/8
```

🔹 **Use Case:** Used in **mathematics, scientific calculations, and symbolic computation**.

---

# **7️⃣ `random` Module (Generating Random Numbers)**
Python's `random` module generates **random numbers** for simulations, gaming, cryptography, and testing.

### **Basic Random Numbers**
```python
import random

print(random.randint(1, 10))  # Random integer from 1 to 10
print(random.random())        # Random float between 0 and 1
print(random.uniform(1, 5))   # Random float between 1 and 5
```

### **Random Choice & Shuffle**
```python
items = [10, 20, 30, 40]
print(random.choice(items))  # Randomly picks one element

random.shuffle(items)  # Shuffles the list
print(items)
```

🔹 **Use Case:** Used in **games, simulations, AI (Monte Carlo), and cryptography**.

---

# **8️⃣ Complex Number Operations**
Python supports advanced complex number operations using the `cmath` module.

### **Example:**
```python
import cmath

z = 1 + 2j  # Complex number

print(cmath.polar(z))    # Convert to polar form (r, theta)
print(cmath.rect(2, cmath.pi/4))  # Convert from polar to rectangular
print(cmath.exp(z))      # Exponential of a complex number
print(cmath.log(z))      # Logarithm of a complex number
print(cmath.sqrt(-1))    # sqrt(-1) = 1j
```

🔹 **Use Case:** Used in **electrical engineering, signal processing, physics, and quantum computing**.

---

# **9️⃣ Performance Optimization in Number Handling**
Python provides **efficient ways to handle numerical computations**.

### **Using NumPy for Faster Computation**
NumPy is **100x faster** than regular Python lists for numerical operations.

```python
import numpy as np

arr = np.array([1, 2, 3, 4])
print(arr * 2)  # Efficient element-wise operations
```

🔹 **Use Case:** Used in **Data Science, AI, and Machine Learning**.

---

## **✅ Summary: Advanced Number Concepts**
| Concept | Description |
|---------|-------------|
| **Big Integers** | Python supports **arbitrary precision** integers. |
| **Bitwise Operations** | Perform **binary-level** manipulations using `&`, `|`, `^`, `<<`, `>>`. |
| **Infinity & NaN** | Special values for **undefined & infinite numbers**. |
| **decimal Module** | High-precision floating-point arithmetic for **financial applications**. |
| **fractions Module** | Exact **rational number** representation. |
| **random Module** | Generate **random numbers** for cryptography, gaming, and simulations. |
| **cmath Module** | Advanced **complex number** operations. |
| **NumPy Optimization** | Speeds up **numerical operations** significantly. |

Python provides a **powerful numerical ecosystem** that makes it suitable for **scientific computing, AI, cryptography, and high-precision applications**. 🚀

