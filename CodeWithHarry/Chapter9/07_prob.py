with open("poem.txt") as f :
    data = f.read()
    if("twinkle" in data):
        print("twinkle is present in poem")
    else:
         print("twinkle is not present in poem")
    