a, b, c = input().split(), input().split(), input().split()
print(c[0] if a[0] == b[0] else (a[0] if a[0] != c[0] else b[0]),
      c[1] if a[1] == b[1] else (a[1] if a[1] != c[1] else b[1]))
