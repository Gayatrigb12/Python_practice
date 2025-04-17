# Using walrusOperator
"""
🦭 Walrus Operator (:=) in Python:

The walrus operator allows you to assign a value to a variable while using it in an expression.

🟢 Introduced in Python 3.8
🛠️ Syntax: variable := expression
"""
if (n:= len([1,2,3,4,5]))>3:
    print(f"List is too long {n} elemenys , expected <=3")