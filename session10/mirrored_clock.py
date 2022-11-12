time = [int(i) for i in input().split()]
hh = f'{12 - time[0]:02d}' if time[0] != 00 else '00'
mm = f'{60 - time[1]:02d}' if time[1] != 00 else '00'
print(f'{hh}:{mm}')
