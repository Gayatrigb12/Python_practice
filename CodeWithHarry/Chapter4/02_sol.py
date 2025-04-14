
# take marks of 6 stud and sort them 
marks = []
for i in range(1,7):
    s = int(input(f"Enter Marks of student {i} : "))
    marks.append(s)
marks.sort()
print(marks)