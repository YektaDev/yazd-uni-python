import math

n = int(input())
halfCeil = math.ceil(n / 2)
print((halfCeil + 1) ** 2 if n % 2 == 0 else (halfCeil ** 2) + halfCeil)
