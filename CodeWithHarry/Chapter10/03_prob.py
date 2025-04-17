class Programmer:
    comp = "Microsoft"
    
    def __init__(self , name , sal , pincode):
        self.sal = sal
        self.name = name
        self.pincode = pincode
p1 = Programmer("Gayatri" , 123456789 ,234567)
print(p1.comp , p1.name , p1.sal , p1.pincode) 
p2 = Programmer("Krish" , 987654321 ,234567)
print(p2.comp , p2.name , p2.sal , p2.pincode)   