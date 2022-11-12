count = [int(i) for i in input().split()]
bottles, volume = count[0], count[1]
for i in range(bottles):
    volume -= int(input())
if volume <= 0:
    print("YES")
else:
    print("NO")
