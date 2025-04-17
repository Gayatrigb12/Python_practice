class Employee:
    company ="VK"
    def show(self):
        print(f" The name is {self.name} and salary is {self.salary}")
# class Programmer:
#     company ="ITC infotech"
#     def show(self):
#         print(f" The name is {self.name} and salary is {self.salary}")
#     def show_lang(self):
#         print(f" The name is {self.name} and Language  is {self.lang}")

class Programmer(Employee):
    company ="ITC infotech"
    def show_lang(self):
        print(f" The name is {self.name} and Language  is {self.lang}")

a = Employee()
b = Programmer()

print("Employee : ", a.company ,"Programmer : ", b.company)