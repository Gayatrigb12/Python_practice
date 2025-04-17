# create virtual env 

# Install Venv
## S1
pip install virtualenv # for installing venv
## s2 
pip --version # checking version 
## s3 
python -m venv env
 #Use built-in venv instead (Recommended for Python 3.3+)

    --- OR ----

virtualenv env

This will create a folder called env with your virtual environment inside.

# install new version
## open chapter 13 folder in terminal and 
## install pandas another version 

---> Microsoft Windows [Version 10.0.22000.2538]
(c) Microsoft Corporation. All rights reserved.

D:\PYTHON\Python_practice\CodeWithHarry\Capter13>pip install pandas
Defaulting to user installation because normal site-packages is not writeable
Requirement already satisfied: pandas in c:\users\acer\appdata\roaming\python\python313\site-packages (2.2.3)
Requirement already satisfied: numpy>=1.26.0 in c:\users\acer\appdata\roaming\python\python313\site-packages (from pandas) (2.2.4)
Requirement already satisfied: python-dateutil>=2.8.2 in c:\users\acer\appdata\roaming\python\python313\site-packages (from pandas) (2.9.0.post0)
Requirement already satisfied: pytz>=2020.1 in c:\users\acer\appdata\roaming\python\python313\site-packages (from pandas) (2025.2)
Requirement already satisfied: tzdata>=2022.7 in c:\users\acer\appdata\roaming\python\python313\site-packages (from pandas) (2025.2)
Requirement already satisfied: six>=1.5 in c:\users\acer\appdata\roaming\python\python313\site-packages (from python-dateutil>=2.8.2->pandas) (1.17.0)

[notice] A new release of pip is available: 24.3.1 -> 25.0.1
[notice] To update, run: python.exe -m pip install --upgrade pip



## -- then install new -- pip install pandas==1.5.2
----->D:\PYTHON\Python_practice\CodeWithHarry\Capter13>pip install pandas==1.5.2
Defaulting to user installation because normal site-packages is not writeable
Collecting pandas==1.5.2
  Downloading pandas-1.5.2.tar.gz (5.2 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 5.2/5.2 MB 10.8 MB/s eta 0:00:00
  Installing build

# How to activate Venv

in terminal 

## .\env\Scripts\Activate.ps1



# pip freeze 

PS D:\PYTHON\Python_practice\CodeWithHarry\Chapter13>  pip freeze
comtypes==1.4.10
distlib==0.3.9
filelock==3.18.0
numpy==2.2.4
pandas==2.2.3
platformdirs==4.3.7
pypiwin32==223
python-dateutil==2.9.0.post0
pyttsx3==2.98
pytz==2025.2
pywin32==310
six==1.17.0
tzdata==2025.2
virtualenv==20.30.0
PS D:\PYTHON\Python_practice\CodeWithHarry\Chapter13> 

# pip freeze op store in file 

PS D:\PYTHON\Python_practice\CodeWithHarry\Chapter13>  pip freeze > requiredment.txt 


# Lamda function

Haha 😄 looks like you meant **"lambda function"** in Python (maybe typo: *amda → lambda*) — and yes, it can be fun too!

---

## 🐍 What is a **lambda function** in Python?

A **lambda function** is a **small, anonymous function** — used for quick operations without formally defining a function.

---

### 🔧 Syntax:
```python
lambda arguments: expression
```

---

### ✅ Example 1: Simple sum
```python
add = lambda a, b: a + b
print(add(3, 5))  # Output: 8
```

---

### ✅ Example 2: Sorting with lambda
```python
students = [("Gayatri", 80), ("Aman", 90), ("Neha", 75)]
students.sort(key=lambda x: x[1])
print(students)
```

📤 Sorts based on marks (second item in tuple).

---

### ✅ Example 3: With `map()`
```python
nums = [1, 2, 3, 4]
squares = list(map(lambda x: x**2, nums))
print(squares)  # [1, 4, 9, 16]
```

---

## 🤓 When to use `lambda`:
- One-liner functions
- Temporary functions (like for `map`, `filter`, `sort`, etc.)
- When you don’t want to name a full function

---

Want to try writing one together? Or want a mini challenge using `lambda`?