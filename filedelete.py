import os

file=input("which file do you want to delete : ")

if os.path.exists(file):
    os.remove(file)
    print("file deleted successfully...")
else:
    print(f"{file} no file")