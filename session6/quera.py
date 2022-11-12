daysOccupied = set()
for i in range(3):
    input()
    daysOccupied.update(input().split())
print(7 - len(daysOccupied))
