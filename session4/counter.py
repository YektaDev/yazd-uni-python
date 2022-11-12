stars = 0
lineCount = int(input().split(" ")[0])
for i in range(lineCount):
    stars += input().count('*')
print(stars)
