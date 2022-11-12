for i in range(int(input())):
    x, y = map(int, input().split())
    if x != y and x - y != 2:
        print("-1")
        continue
    if x % 2 == 0 and y % 2 == 0:
        print(x + y)
    elif x % 2 == 1 and y % 2 == 1:
        print(x + y - 1)
    else:
        print("-1")
