p1 = "good"
p2 = "bad"
p3 =  "happy"
p4 = "sad"

msg = input("Enter message : ")

if((p1 in msg) or (p2 in msg) or (p3 in msg) or (p4 in msg)):
    print(" Spam message  !")
else:
    print("not a Spam message  !")