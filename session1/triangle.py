angles = [int(numberStr) for numberStr in input().split()]

anglesAreNotZero = angles[0] != 0 and angles[1] != 0 and angles[2] != 0
anglesHaveCorrectSum = angles[0] + angles[1] + angles[2] == 180

if anglesAreNotZero and anglesHaveCorrectSum:
    print("Yes")
else:
    print("No")
