input()
weights = [int(i) for i in input().split()]
max = max(weights)
for i in range(len(weights) - 1, -1, -1):
    if weights[i] != max: continue
    print(i + 1)
