number = int(input())
i = 0
while True:
    power = 2 ** i
    i += 1
    if power > number:
        print(power)
        break
