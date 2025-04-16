# Get marks from user
marks = float(input("Enter your marks (out of 100): "))

# Grade calculation logic
if marks >= 90:
    grade = 'A+'
elif marks >= 80:
    grade = 'A'
elif marks >= 70:
    grade = 'B+'
elif marks >= 60:
    grade = 'B'
elif marks >= 50:
    grade = 'C'
elif marks >= 40:
    grade = 'D'
else:
    grade = 'F'

# Display the result
print(f"Your grade is: {grade}")
