password = len(input("Enter your password: "))
 
if password < 6:
    print("weak password")
elif password >= 6 and password < 11:
    print("medium password")
else:
    print("strong password")
    
