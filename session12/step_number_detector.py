n = input("Enter a number: ").strip()
if len(n) == 1:
    print("It's a `step!` number.")
    exit(0)
step = abs(int(n[1]) - int(n[0]))
for i in range(2, len(n)):
    if abs(int(n[i]) - int(n[i - 1])) != step:
        print("Not a `step!` number.")
        exit(0)
print("It's a `step!` number.")
