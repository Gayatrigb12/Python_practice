class Employee:
    a = 1
    def show(self):
        print(f"class value is {self.a}")
    @classmethod
    def show(cls):
        print(f"class value is {cls.a}")

    @property
    def name(self):
        return f"{self.fname} {self.lname}"
    
    # @name.setter
    # def name(self , value):
    #     self.ename  = value
    
    @name.setter
    def name(self , value):
        self.fname  = value.split(" ")[0]
        self.lname  = value.split(" ")[1]
e = Employee()
e.a = 45

e.name = "gayatri Bagul"
print(e.name)

e.show()