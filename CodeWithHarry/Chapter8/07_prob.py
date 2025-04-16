list = ["Aarohi", "Isha", "Meera", "Anaya", "Saanvi", "Diya", "Kavya", "Riya"]

def remove(list,word):
    n = []
    for i in list:
        if not(i == word):
            n.append(i.strip(word))
    return n
print(remove(list , "ya"))