# A piece of code that reads two files and checks if their content is equal or not.

with open(input("Enter the name or address of the first file: "), mode="r", encoding="utf-8") as f1, \
        open(input("Enter the name or address of the second file: "), mode="r", encoding="utf-8") as f2:
    print("The same." if f1.readlines() == f2.readlines() else "Not the same.")
