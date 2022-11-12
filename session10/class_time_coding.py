# Functions
def fibo1(n):
    """Prints a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()


# Print the function docstring:
# print(help(fibo1))
# Call the function:
fibo1(100)


def fibo2(n):
    """Returns a list containing the Fibonacci series up to n."""
    a, b = 0, 1
    result = []
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result


# Call the function:
print(fibo2(100))


def my_function(name):
    print('Hello ' + name)


my_function('Ali')


def my_function2(fname, lname):
    print(fname + ' ' + lname)


my_function2('Ali', 'Khaleqi Yekta')


# my_function2('Ali') Misses 1 argument


# Functions with default values
def my_function3(fname, lname='Khaleqi Yekta'):
    print(fname + ' ' + lname)


my_function3('Ali', 'Khaleqi Yekta')
my_function3('Ali')  # Now this is OK!


# Default values for arguments are mutable objects
def f(a, list1=[]):
    list1.append(a)
    return list1


print(f(1))
print(f(2))
print(f(3))

# Keyword Arguments
# You can also send arguments with the key = value syntax. This way the order of the arguments does not matter.
my_function2(lname='Khaleqi Yekta', fname='Ali')


# Arbitrary Arguments
# If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the
# function definition. This way the function will receive a tuple of arguments, and can access the items accordingly:
def greet(*names):
    """This function greets all the person in the names tuple."""
    # names is a tuple with arguments
    for name in names:
        print('Hello', name)


greet('Ali', 'Reza', 'Sara')


# Arbitrary Keyword Arguments
# If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the
# parameter name in the function definition. This way the function will receive a dictionary of arguments, and can
# access the items accordingly:
def my_function4(**person):
    print('His last name is ' + person['lname'])


my_function4(fname='Ali', lname='Khaleqi Yekta')


# Positional-Only or Keyword-Only
# You can specify that a function argument must be passed as a keyword argument, or a positional argument.
# This is done by placing / or * in the function definition.
def my_function5(a, /, b, *, c):
    print(a, b, c)


my_function5(1, 2, c=3)


# Recursive Function
def factorial(n):
    """This is a recursive function to find the factorial of an integer."""
    if n == 1:
        return n
    else:
        return n * factorial(n - 1)


num = 5
print('The factorial of', num, 'is', factorial(num))

# Lambda Function
# A lambda function is a small anonymous function. A lambda function can take any number of arguments, but can only have
# one expression. Syntax: lambda arguments: expression where expression is executed and result is returned. You can
# assign the lambda function to a variable, in which case it can be used like a normal function. Lambda functions are
# used along with built-in functions like filter(), map() etc. The filter() function in Python takes in a function and a
# list as arguments. The function is called with all the items in the list and a new list is returned which contains
# items for which the function evaluates to True.
y = lambda a, b, x: a * x + b
print(y(2, 3, 5))


def myfunc(n):
    return lambda a: a * n


mydoubler = myfunc(2)
mytripler = myfunc(3)
print(mydoubler(11))
print(mytripler(11))

# Scope
# in Python, the scope of a variable is the region of the program where the variable is recognized. There are two basic
# scopes of variables in Python, global and local. A variable that is defined inside a function is local to that
# function. A variable that is defined outside of a function is global. A global variable can be accessed inside or
# outside of a function.
x = 1


def func():
    print('inside x:', x)


func()
print('outside x:', x)


# A variable declared inside the function's body or in the local scope is not visible from outside the function.
def func2():
    x_local = 2
    print('inside x:', x_local)


func2()


# print('outside x:', x_local) This leads to an error


# global Keyword
def func2():
    global x_local  # This makes x_local global
    x_local = 2
    print('inside x:', x_local)


func2()
print('outside x:', x_local)  # Now this is OK!

# Local AND global variables
x = 5


def func():
    x = 10
    print('local x:', x)


func()
print('global x:', x)

# Example 1
x = 10


def func(x):
    x = 5


func(x)
print(x)
# Example 2
x = [10, 11, 12]


def func(x):
    x[0] = 5


func(x)
print(x)
# Example 3
x = [10, 11, 12]


def func(x):
    x[0] = 5


func(x.copy())
print(x)

# Built-in Functions
# Python has a set of built-in functions, including print(), input(), etc. You can find a complete list of Python's
# built-in functions here: https://docs.python.org/3/library/functions.html

# abs(x)
# The abs() function returns the absolute (positive) value of the specified number. The argument may be an integer or a
# floating point number. If the argument is a complex number, its magnitude is returned. abs() is a built-in function.
print(abs(-5))

# all(iterable)
# The all() function returns True if all items in an iterable object are true, otherwise it returns False. If the
# iterable object is empty, the all() function also returns True. all() is a built-in function.
l = [1, 2, 3, 4, 5]
print(all(i > 0 for i in l))

# any(iterable)
# The any() function returns True if any item in an iterable object is true, otherwise it returns False. If the iterable
# object is empty, the any() function also returns False. any() is a built-in function.
l = [1, 2, 3, 4, 5]
print(any(i % 2 == 0 for i in l))

# bin(x)
# The bin() function converts and returns the binary equivalent string of a given integer. If the parameter is not an
# integer, it has to implement __index__() method to return an integer. bin() is a built-in function.
print(bin(12))

# chr(i)
# The chr() function returns a character (a string) from an integer (represents unicode code point of the character).
# chr() is a built-in function.
print(chr(97))

# divmod(a, b)
# The divmod() function takes two numbers and returns a pair of numbers (a tuple) consisting of their quotient and
# remainder. The quotient is the integer value of the quotient. The remainder is the value of the remainder. divmod()
# is a built-in function.
print(divmod(31, 8))

# hex(x)
# The hex() function converts an integer number to a lowercase hexadecimal string prefixed with “0x”. If the parameter
# isn’t an integer, it has to implement __index__() method to return an integer. hex() is a built-in function.
print(hex(12))

# map(function, iterable, ...)
# The map() function executes a specified function for each item in an iterable. The item is sent to the function as a
# parameter. map() is a built-in function.
double = lambda x: x * 2
l = [1, 2, 3, 4, 5]
print(*map(double, l))

# max(iterable) or max(*args)
# The max() function returns the largest item in an iterable or the largest of two or more arguments. max() is a
# built-in function.
l = [1, 2, 3, 4, 5]
print(max(l))

# oct(x)
# The oct() function converts an integer number to an octal string prefixed with “0o”. If the parameter isn’t an
# integer, it has to implement __index__() method to return an integer. oct() is a built-in function.
print(oct(12))

# pow(x, y[, z])
# The pow() function returns the value of x to the power of y (xy). If z is present, it returns x to the power of y,
# modulus. pow() is a built-in function.
print(pow(2, 3))

# reversed()
# Returns a reversed iterator. reversed() is a built-in function.
l = [1, 2, 3, 4, 5]
print(*reversed(l))

# round(number[, ndigits])
s = 'hello'
print(round(2.675))
print(round(2.675, 2))

# sum(iterable[, start])
# The sum() function adds the items of an iterable and returns the sum. The start parameter is not necessary and
# defaults to 0 if not specified. sum() is a built-in function.
l = [1, 2, 3, 4, 5]
print(sum(l))
