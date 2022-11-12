# A piece of code that copies all the contents of one file to another file.

with open(input("Enter the name or address of source file: "), mode="r", encoding="utf-8") as f1, \
        open(input("Enter the name or address of the destination file: "), mode="w", encoding="utf-8") as f2:
    f2.writelines(f1.readlines())
print("Done!")
