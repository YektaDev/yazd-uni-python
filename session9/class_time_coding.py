n = int(input())
counter = 2
while n % counter != 0 and counter < n:
    counter += 1
    if counter == n:
        print(f'{n} Is Prime')
    else:
        print(f'{n} Is not Prime')
        break

# With the break statement we can stop the loop even if the while condition is True:
l = ['hello', 'python', 'exit', 'pizza']
index = 0
while index < len(l):
    print(l[index])
    if l[index] == 'exit':
        break
    index += 1

# continue
# With the continue statement we can stop the current iteration, and continue with the next:
counter = 0
while counter < 10:
    counter += 1
    if counter % 2 == 0:
        continue
    print(counter)

# while else
l = ['hello', 'python', 'exit', 'pizza']
index = 0
while index < len(l):
    if l[index] == 'exit':
        print('exit')
        break
    index += 1
else:
    print('There is no "exit" in l')

# while else again, just a different list!
l = ['hello', 'python', 'skip', 'pizza']
index = 0
while index < len(l):
    if l[index] == 'exit':
        print('exit')
        break
    index += 1
else:
    print('There is no "exit" in l')
# for
# The for loop in Python is used to iterate over a sequence (list, tuple, string) or other iterable objects.
# Iterating over a sequence is called traversal.
interests = ['rain', 'pizza', 'football', 'python']
for i in interests:
    print(i)
# Nested loop
# A nested loop is a loop inside a loop. The "inner loop" will be executed one time for each iteration of the
# "outer loop":
interests = ['rain', 'pizza', 'football', 'python']
for i in interests:
    for ch in i:
        print(ch, end='_')
    print()
# Another example!
interests = ['rain', 'pizza', 'football', 'python']
for i in interests:
    print(i, sep='_')
# break
# With the break statement we can stop the loop before it has looped through all the items.

# continue
l = ['hello', 'python', 'skip', 'pizza']
for w in i:
    pass

# for-else
# A for loop can have an optional else block as well.
l = [1, 2, 3, 4, 5, 6, 7, 8]
for i in l:
    if i == 8:
        print('8')
        break
else:
    print('There is no 8 in l')

l = [1, 2, 3, 4, 5, 6, 7]
for i in l:
    if i == 8:
        print('8')
        break
else:
    print('There is no 8 in l')

# range(start, end, step)
# To loop through a set of code a specified number of times, we can use the range() function, The range() function
# returns a sequence of numbers, starting from 0 by default, and increments by 1, (by default), and ends at a specified
# number.
print(list(range(10)))
print(list(range(1, 10, 2)))
print(list(range(10, 0, -1)))
# You can also do:
print(list(range(1, 10, 2)))
print(range(1, 10, 2)[3])
print(range(10, 0, -1)[1])
# So in equality of lists created by ranges,
print(list(range(0, 3, 2)))
print(list(range(0, 4, 2)))
print(range(0, 3, 2) == range(0, 4, 2))

# enumerate
# Returns an enumerate object. Iterable must be a sequence, an iterator, or some other object which supports
# iteration.
season = ['Spring', 'Summer', 'Fall', 'Winter']
for a, b in enumerate(season):
    print(a, b)
print('-' * 20)
for a, b in enumerate(season, start=1):
    print(a, b)
