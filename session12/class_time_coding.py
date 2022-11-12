# Math
import math

# dir - list of attributes and methods
print(dir(math))

# math.ceil - round up
print(math.ceil(3.5))
print(math.ceil(-3.4))

# math.trunc vs int
print(math.trunc(-0.925))
print(int(-0.925))  # The same as trunc

# math.comb(n, k) - number of ways to choose k items from n items without repetition and without order
print(math.comb(10, 4))
print(math.comb(10, 6))

# math.floor - round down
print(math.floor(3.5))
print(math.floor(-3.4))

# math.fsum - sum of floats
print(math.fsum([1.1, 2.2, 3.3, 4.4, 5.5]))

# itertools Methods
import itertools as iter

h = 'hello'
w = 'world'
print(*list(iter.chain(h, w)))

# iter.combinations(iterable, r) - r-length tuples, in sorted order, no repeated elements
print(*list(iter.combinations('ABCD', 2)))

# iter.combinations_with_replacement(iterable, r) - r-length tuples, in sorted order, with repeated elements
print(*list(iter.combinations_with_replacement('ABCD', 2)))

# iter.accumulate(iterable[, func]) - returns an iterator over the results of applying the function to the previous
# result and the current item from the iterable
import operator

a = [2, 4, 6, 8, 10]
print(*list(iter.accumulate(a)))
print(*list(iter.accumulate(a, operator.mul)))

# iter.product(*iterables, repeat=1) - returns the cartesian product, equivalent to a nested for-loop
# Cartesian product: A × B = {(a, b) : a ∈ A and b ∈ B}
import random

A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
B = ['♠', '♥', '♦', '♣']
l = list(iter.product(A, B))
random.shuffle(l)
person = {
    'p1': l[:13],
    'p2': l[13:26],
    'p3': l[26:39],
    'p4': l[39:52]
}
print(*person.values(), sep='\n')
# print(*list(iter.product(A, B)))
# print(*list(iter.product(A, B, repeat=2)))

import datetime

now = datetime.datetime.now()
print(now)
print(now.strftime('%Y-%m-%d %H:%M:%S'))
print(now.year)
print(now.month)
print(now.day)

# Time difference
t1 = datetime.date(year=1998, month=6, day=19)
t2 = datetime.date.today()
print(t2 - t1)
