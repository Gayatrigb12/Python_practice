class Employee:
    name = "gayatri"
    lang = "java"
    salary = "123456789"
    #constructer
    def __init__(self , name , salary , lang):# Dunder method which are start with double underscrol
        self.salary=salary
        self.lang = lang
        self.name = name
        print("i am creating an object")
        
    
    def getInfo(emp):# use self you can use any word like emp but use self 
        print("get info " , emp.lang , emp.name , emp.salary)
    
    @staticmethod
    def greet():# no need to add self 
        print("Good morning")
        
    
e = Employee("Krishna", "hindi",1234567899)

e.lang = "py"
print(e.lang , e.name , e.salary )

e.getInfo()
e.greet()