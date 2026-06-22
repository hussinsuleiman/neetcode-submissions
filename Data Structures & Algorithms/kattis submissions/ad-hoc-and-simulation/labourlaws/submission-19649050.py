t = int(input())

if t <= 360:
    print(0)
elif t <= 390:
    print(t-360)
elif t <= 570:
    print(30)
elif t <= 585:
    print(t-540)
elif t <= 645:
    print(45)
else:
    print(t-600)