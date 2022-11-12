# A piece of code that reads a file and counts the number of words in it.

with open(input("Enter the name or address of the file: "), mode="r", encoding="utf-8") as f:
    print(len(f.read().split()))
