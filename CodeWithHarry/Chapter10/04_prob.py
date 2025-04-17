class Calculator:
    def __init__(self, num):
        self.num = num
    
    def square(self):
        print(f"The Square of {self.num} is {self.num*self.num}")
        
    def cube(self):
        print(f"The Cube of {self.num} is {self.num*self.num*self.num}")
        
    def squareRoot(self):
        print(f"The Square Root of {self.num} is {self.num**1/2}")
        
    @staticmethod
    def greet():# no need to add self 
        print("Good morning")
        
a = Calculator(8)
a.greet()
a.square()
a.cube()
a.squareRoot()