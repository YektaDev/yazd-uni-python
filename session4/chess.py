realCount = [1, 1, 2, 2, 2, 8]
numbers = [int(i) for i in input().split(" ")]

for i in range(6):
    print(realCount[i] - numbers[i], end=' ')
