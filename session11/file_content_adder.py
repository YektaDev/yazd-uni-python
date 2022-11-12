# A piece of code that reads the content of a file and another file, and adds both of the contents to a third file.

with open(input("Enter the name or address of the first source file: "), mode="r", encoding="utf-8") as f1, \
        open(input("Enter the name or address of the second source file: "), mode="r", encoding="utf-8") as f2, \
        open(input("Enter the name or address of the destination file: "), mode="w", encoding="utf-8") as f3:
    f3.writelines(f1.readlines() + f2.readlines())
print("Done!")
