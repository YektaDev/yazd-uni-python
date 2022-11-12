n, i = int(input()), 1
spaces = int(n / 2)
while i < n:
    print(f"{' ' * spaces}{'*' * i}{' ' * (spaces * 2)}{'*' * i}")
    i += 2
    spaces -= 1
while i > 0:
    print(f"{' ' * spaces}{'*' * i}{' ' * (spaces * 2)}{'*' * i}")
    i -= 2
    spaces += 1
