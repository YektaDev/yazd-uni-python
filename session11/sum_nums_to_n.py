# A piece of code that sums all nums from 1 to n.

n = int(input("Enter a number: "))
sum = 0
for i in range(1, n + 1):
    sum += i
print(sum)
