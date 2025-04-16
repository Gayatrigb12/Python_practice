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
