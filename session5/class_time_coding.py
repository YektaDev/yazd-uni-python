tuple = (4,)  # Exactly like list, but immutable
notTuple1 = (4,)
notTuple2 = 4
print(f'{type(tuple)} {type(notTuple1)} {type(notTuple2)}')

tuple = (1, 2, 3)
print(tuple)
print(*tuple)

# Removing duplications via sets
alpha = {'a', 'b', 'c', 'd', 'a'}
nums = [1, 2, 3, 4, 2, 3, 1, 4]
print(alpha)
print(list(set(nums)))

# Empty collections
emptyList = list()
emptyList = []

# emptyTuple = tuple()
emptyTuple = ()

emptySet = set()
# emptySet = {} This creates an empty map

# Find similar elements
a = {1, 2, 3}
b = {4, 5, 3}

for i in a:
    if b.__contains__(i):
        print(i)

# Add operation
alpha = {'a', 'b', 'c'}
alpha.add('d')
print(alpha)

# Update operation (batch adding / adding a group of elements)
alpha = {'a', 'b', 'c'}
alpha.update('xcvbn')
print(alpha)

# Remove operation (if it doesn't exist, throws an exception)
alpha = {'a', 'b', 'c'}
alpha.remove('c')
print(alpha)

# Safe remove operation (if it doesn't exist, does nothing)
alpha = {'a', 'b', 'c'}
alpha.discard('c')
alpha.discard('d')
print(alpha)

# Pop
alpha = {'a', 'b', 'c'}
a = alpha.pop()
print(a)
print(alpha)

# Remove all elements from the set
alpha = {'a', 'b', 'c'}
alpha.clear()
print(alpha)

# Subset and superset
alpha = {'a', 'b', 'c'}
b = {'b'}
moreAlpha = {'a', 'b', 'c', 'd', 'e', 'f'}
print(alpha.issuperset(b))
print(alpha.issubset(moreAlpha))

# Disjoint
a = {2, 4}
b = {1, 3}
print(a.isdisjoint(b))

# Difference of two sets
a = {1, 2, 3}
b = {1, 2}
print(a.difference(b))  # a - b
print(a - b)  # a - b

# Difference update
a = {1, 2, 3}
b = {1, 2}
print(a.difference_update(b))  # a = a - b

# Intersection of sets
a = {1, 2, 3, 4}
b = {1, 2, 6}
print(a.intersection(b))
print(a & b)

# Intersection update
a = {1, 2, 3, 4}
b = {1, 2, 6}
print(a.intersection_update(b))  # a = a & b

# Symmetric difference (A Δ B) (Returns all the items present in given sets, except the items in their intersections.)
a = {'a', 'b', 'c', 'd'}
b = {'c', 'd', 'e'}
print(a.symmetric_difference(b))  # a Δ b

# Symmetric difference update (A = A Δ B)
a = {'a', 'b', 'c', 'd'}
b = {'c', 'd', 'e'}
print(a.symmetric_difference_update(b))  # a = a Δ b

# Union of n sets
a = {'p', 'y', 't'}
b = {'h', 'o', 'n'}
c = {'s', 't'}
print(a.union(b, c))  # a | b | c
print(a | b | c)

# Frozenset (Returns an immutable frozenset object)
A = frozenset([4, 3, 2, 1])
B = frozenset([7, 6, 5, 4])
C = frozenset([5, 4])
D = A.copy()
print("Copy of frozen set: ", D)
print("Union of frozen set: ", A.union(B))
print("Intersection of frozen set: ", A.intersection(B))
print("Difference of frozen set: ", A.difference(B))
print("symmetric_difference of frozen set: ", A.symmetric_difference(B))
print("disjoint of frozen set: ", A.isdisjoint(C))
print("subset of frozen set: ", C.issubset(B))


# ====================================================== Exercise ======================================================
def get_max_char_freq(word):
    count_all = []
    for i in word:
        count_all.append(word.count(i))
    return max(count_all)


a = ['aaep', 'aspsppp', 'z bca']
a.sort(key=get_max_char_freq, reverse=True)
print(a)

# Dictionary
# A dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly
# brackets, and they have keys and values.
# {key:value, key:value, key:value}
# Keys must be unique, Access syntax: dict[key]
# Values can be of any type, but keys must be of an immutable data type such as strings, numbers, or tuples.
# Get the count of current elements in the dictionary: len(dict)
dictionary = {1: 'a', 2: 'b', 3: 'c'}

for item in dictionary.keys():
    print(item)
for item in dictionary.values():
    print(item)
for i, j in dictionary.items():
    print(i, j)

# ====================================================== Exercise ======================================================
mydict1 = {'water': 'آب', 'book': 'کتاب', 'he': 'او'}
mydict2 = {}
for key, value in mydict1.items():
    mydict2[value] = key
print(mydict2)

# Dictionary methods
# Clear
a = {'a': 1, 'b': 2, 'c': 3}
a.clear()

# Copy
# This is a shallow copy, so if the dictionary contains any mutable objects,
# a reference to the object will be copied instead.
a = {'a': 1, 'b': 2, 'c': 3}
b = a.copy()

# Deep copy
a = {'a': 1, 'b': 2, 'c': 3}
import copy as cp

b = cp.deepcopy(a)

# Fromkeys
# Creates a new dictionary with keys from seq and values set to value.
a = {'a': 1, 'b': 2, 'c': 3}
b = a.fromkeys(['a', 'b', 'c'], 0)
print(b)

# Converting two lists into a dictionary
keys = ['a', 'b', 'c']
values = [1, 2, 3]
dictionary = dict(zip(keys, values))
print(dictionary)  # {'a': 1, 'b': 2, 'c': 3}

# Finding all prime numbers in (a,b)
a = 8
b = 20
result = []
for num in range(a + 1, b + 1):
    if all(num % i != 0 for i in range(2, num)) or num == 2:
        result.append(num)

# Printing elements of a list separated by comma
print(','.join(map(str, result)))

a = [1, 2, 3]
b = [4, 5, 6]
c = [x + y for x, y in zip(a, b)]
print(c)
