input()
errors = 0
for a1, a2 in zip(input(), input()):
    if a1 != a2: errors += 1
print(errors)
