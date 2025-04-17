class Demo:
    a = 4
o = Demo()
print(o.a) # printing class attribute because instace attribute is not present 
o.a = 0 # initilize instace attribute 
print(o.a) # instance attribute is print 
print(Demo.a) # class attribute is printed 