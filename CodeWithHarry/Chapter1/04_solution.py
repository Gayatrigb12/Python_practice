import os

# Get the path of the directory (you can modify this)
directory_path = input("Enter the path of the directory: ")

try:
    # List all files and directories in the given path
    contents = os.listdir(directory_path)

    print(f"\nContents of '{directory_path}':")
    for item in contents:
        print(item)
except FileNotFoundError:
    print("The specified directory does not exist.")
except PermissionError:
    print("You do not have permission to access this directory.")
