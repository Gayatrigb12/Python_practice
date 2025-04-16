# TEmprature 


def temprature(f):
    return 5*(f-32)/9

f = int(input("enter temp in F : "))
print(f"{f} feheranhit is {round(temprature(f), 2)} °C")
