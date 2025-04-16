sub1 = int(input("Enter sub 1 marks : "))
sub2 = int(input("Enter sub 2 marks : "))
sub3 = int(input("Enter sub 3 marks : "))

total_percentage = ((sub1 + sub2 + sub3 )*100 )/300

if(total_percentage>=40 and sub1 >= 33 and sub2>=33 and sub3>=33):
    print(f"Pass {total_percentage} % !")
else:
    print(f"Fail {total_percentage} % ! try next year .")
