nums = [int(i) for i in input().split(" ")]
delay1, delay2, totalSteps = nums[0], nums[1], nums[2]

if totalSteps % 2 == 0:
    halfSteps = totalSteps / 2
    timeTaken = halfSteps * delay1 + halfSteps * delay2
if totalSteps % 2 == 1:
    timeTaken = (halfSteps + 1) * delay1 + halfSteps * delay2

print(int(timeTaken))
