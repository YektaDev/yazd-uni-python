num = int(input('Please enter an integer:'))
if num < 0:
    print('Negative')
elif num == 0:
    print('Zero')
else:
    print('Positive')

# Python interprets non-zero values as True. Zero or empty values are interpreted as False.
num = int(input('Please enter an integer:'))
if num == 0:
    print('Zero')
elif num + abs(num):
    print('Positive')
else:
    print('Negative')

# Nested if
# We can have if statements inside "if" statements, this is called nesting in computer programming.
num = int(input('Please enter an integer:'))
if num + abs(num):
    if num % 2:
        print('Odd Positive')
    else:
        print('Even Positive')
else:
    if num % 2:
        print('Odd Negative')
    else:
        print('Even Negative')

# Compound if
# If you have only one statement to execute, you can put it on the same line as the if statement.
a = 10
b = 20
if a > b: print('a is greater than b')
print('a is greater than b') if a > b else print('a is less than or equal to b')

# Pass statement
# if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass
# statement to avoid getting an error.
a = 10
b = 5
if b > a:
    pass


# match Statement
# A match statement takes an expression and compares its value to successive patterns given as one or more case blocks.
def http_error(status_code):
    match status_code:
        case 400:
            return 'Bad Request'
        case 401:
            return 'Unauthorized'
        case 403:
            return 'Forbidden'
        case 404:
            return 'Not Found'
        case 500:
            return 'Internal Server Error'
        case _:
            return 'Unknown Error'
