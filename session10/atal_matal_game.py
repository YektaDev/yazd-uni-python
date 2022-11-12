counts = [int(i) for i in input().split()]
n, k, current, rounds = counts[0], counts[1], 0, 0
while current != 0 or not rounds:
    rounds += 1
    current = (current + k) % n
print(rounds)
