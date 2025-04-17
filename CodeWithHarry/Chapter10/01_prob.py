class Employee:
    name = "gayatri"
    lang = "java"
    salary = "123456789"
    
    def getInfo(emp):# use self you can use any word like emp but use self 
        print("get info " , emp.lang , emp.name , emp.salary)
    
    @staticmethod
    def greet():# no need to add self 
        print("Good morning")
        
    
e = Employee()
e.comp = "asdfgh"
e.lang = "py"
print(e.lang , e.name , e.salary , e.comp)

e.getInfo()
e.greet()