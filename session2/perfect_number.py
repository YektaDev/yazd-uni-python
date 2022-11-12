number = int(input())
sumOfDivisors = 0

for i in range(1, number):
    if number % i == 0:
        sumOfDivisors += i

if sumOfDivisors == number:
    print("YES")
else:
    print("NO")
