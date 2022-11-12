foundAny = False
for i in range(1, 6):
    line = input()
    if line.__contains__("MOLANA") or line.__contains__("HAFEZ"):
        foundAny = True
        print(i, end=' ')
