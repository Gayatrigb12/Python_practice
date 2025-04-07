# Reversing a string using a loop
str = input("Enter a string: ")
rev = ""
for char in str:
    rev = char + rev
print("Reversed string:", rev)

