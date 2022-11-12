nums = sorted([int(input()) for i in range(3)])

if nums[0] ** 2 + nums[1] ** 2 == nums[2] ** 2:
    print("YES")
else:
    print("NO")
