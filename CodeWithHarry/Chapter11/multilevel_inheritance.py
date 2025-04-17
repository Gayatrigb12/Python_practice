class Employee:
    a = 1
    def __init__(self):
        print("Constructor of Emp")

class Programmer(Employee):
    b = 2

class Manager(Programmer):
    c = 3
    
emp = Employee()
print(emp.a) # print attribute a
# print(emp.b) # Error no attribute a 
# print(emp.c) # Error no attribute a 
prog = Programmer
print(prog.a , prog.b)

man = Manager()
print(man.a, man.b ,man.c)
