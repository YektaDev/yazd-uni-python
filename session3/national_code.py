isValid = False
# Receives the national code until it is valid
while not isValid:
    code = input("Please enter a national code: ")
    isValid = len(code) == 10 and code.isdecimal()

print("The national code is valid.")
