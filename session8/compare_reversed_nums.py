n1, n2 = input(), input()
r1, r2 = n1[::-1], n2[::-1]
if r1 < r2:
    print(f'{n1} < {n2}')
elif r1 > r2:
    print(f'{n2} < {n1}')
else:
    print(f'{n1} = {n2}')
