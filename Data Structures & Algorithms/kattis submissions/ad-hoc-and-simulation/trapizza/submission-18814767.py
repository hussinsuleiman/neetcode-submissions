import math

d = int(input())
a = int(input())
b = int(input())
h = int(input())

a1 = (d / 2) ** 2 * math.pi
a2 = (a+b) * h / 2

if a1 > a2:
    print("Mahjong!")
elif a1 < a2:
    print("Trapizza!")
else:
    print("Jafn storar!")