class Employee:
    a = 1
    def __init__(self):
        print("Constructor of Emp")

class Programmer(Employee):
    b = 2
    def __init__(self):
        print("Constructor of Prog")


class Manager(Programmer):
    c = 3
    def __init__(self):
        super().__init__()
        print("Constructor of Man")

    
emp = Employee()
print(emp.a) # print attribute a
# print(emp.b) # Error no attribute a 
# print(emp.c) # Error no attribute a 
p = Programmer()
print(p.a , p.b)

man = Manager()
print(man.a, man.b ,man.c)


