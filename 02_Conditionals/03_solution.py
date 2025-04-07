score = float(input("Enter your score: "))

if score < 0 or score > 100:
    print("Invalid score. Please enter a score between 0 and 100.")
    exit() # exit the program if the score is invalid

if score >= 90 and score <= 100:
    grade = "A"
elif score >= 80 and score < 90:
    grade = "B"
elif score >= 70 and score < 80:
    grade = "C"
elif score >= 60 and score < 70:
    grade = "D"
    
else:
    grade = "F"
    
print ("Your grade is:", grade) # print the grade of the user