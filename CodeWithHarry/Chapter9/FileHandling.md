## File Handling 

RAM = (RANDOM ACCESS MEMORY) = volatile 
--> Fast (data lost after operation)
HDD = (Hard Disk Drive ) = non volatile
--> Slow 


# operation using py
--> read (r)

f = open("file.txt")
data = f.read()
print(data)
f.close()


--> write (w)

st = "Om Namah Shivay"
f = open("file.txt" , "w")
f.write(st)
f.close()

--> append (a)

st = "Om Namah Shivay"
f = open("file.txt" , "a")
f.write(st)
f.close()

--> open for updating (+)
f = open("file.txt", "r+")
data = f.read()
print("Before update:", data)

# Replace the content
updated_data = data.replace("Om Namah Shivay", "Shree Shivay Namahstubhyam\n")

# Move cursor back to the beginning
f.seek(0)
f.write(updated_data)
f.truncate()  # Cut off any leftover content after new write
file = open("file.txt", "r+")
new = file.read()
print("After update:", new)

file.close()


--> read in binary mode (rb)

f = open("file.txt","rb")
data = f.read()
print(data)
f.close()

--> read in text mode (rt)

f = open("file.txt","rt")
data = f.read()
print(data)
f.close()



# FUNCTIONS 

# readlines()

--> 
f = open("file.txt")
lines = f.readlines()
print(lines , type(lines)) # list type 

# readline()

