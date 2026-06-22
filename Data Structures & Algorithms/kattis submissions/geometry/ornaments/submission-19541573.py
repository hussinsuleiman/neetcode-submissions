from math import acos, pi
r,h,s = map(int, input().split())

while (r,h,s) != (0,0,0):
    res = (2*r*(pi - acos(r/h)) + 2 * (h**2 - r**2)**0.5) * (1 + s/100)
    print(f"{res:.2f}")
    r,h,s = map(int, input().split())