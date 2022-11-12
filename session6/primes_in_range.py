result = []
for num in range(int(input()) + 1, int(input())):
    if all(num % i != 0 for i in range(2, num)):
        result.append(num)
print(','.join(map(str, result)))
