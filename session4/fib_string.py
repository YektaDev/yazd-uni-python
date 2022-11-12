n = int(input())
fibonacciSeries = [0, 1]
for i in range(2, n + 1):
    fibonacciSeries.append(fibonacciSeries[i - 1] + fibonacciSeries[i - 2])

for i in range(1, n + 1):
    if fibonacciSeries.__contains__(i):
        print('+', end='')
    else:
        print('-', end='')
