class Employee:
    company ="VK"
    name = "abc"
    def show(self):
        print(f" The name is {self.name} and company is {self.company}")
class Coder:
    lang = "Java"
    def printLang(self):
        print(f"out of all languages here is your lang {self.lang} ")
    
class Programmer(Employee , Coder):
    company ="ITC infotech"
    def show_lang(self):
        print(f" The name is {self.company} and Language  is {self.lang}")

a = Employee()
b = Programmer()

b.show()
b.printLang()
b.show_lang()

print("Employee : ", a.company ,"Programmer : ", b.company)