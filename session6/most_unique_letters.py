maxLen = 0
for i in range(int(input())):
    uniqueLettersCount = len(set(input()))
    maxLen = max(maxLen, uniqueLettersCount)
print(maxLen)
