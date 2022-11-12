from math import floor

nums = [int(n) for n in input().split()]
for i in range(nums[1]):
    nums[0] /= 2
print(floor(nums[0]))
