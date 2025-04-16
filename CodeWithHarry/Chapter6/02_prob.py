a = int(input("Enter num a : "))
b = int(input("Enter num b : "))
c = int(input("Enter num c : "))
d = int(input("Enter num d : "))

if(a>b and a>c and a>d):
    print("A is greatter !")
elif(b>a and b>c and b>d):
    print("B is greatter !")
elif(c>a and c>b and c>d):
    print("C is greatter !")
else:
    print("D is greatter !")