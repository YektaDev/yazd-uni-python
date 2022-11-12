reds, yellows, greens = 0, 0, 0
for ch in input():
    if ch == 'R':
        reds += 1
    elif ch == 'Y':
        yellows += 1
    else:
        greens += 1
if reds >= 3 or (reds >= 2 and yellows >= 2) or greens == 0:
    print('nakhor lite')
else:
    print('rahat baash')
