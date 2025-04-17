class Employee:
    a = 1
    def show(self):
        print(f"class value is {self.a}")
    @classmethod
    def show_class(self):
        print(f"class value is {self.a}")

    
e = Employee()
e.a = 45

e.show()
e.show_class()