from math import acos,pi

t = int(input())

for i in range(t):
    R,h1,h2 = map(float, input().split())
    h1, h2 = h1/1000, h2/1000
    print(R*(acos(R/(R+h1)) + acos(R/(R+h2))))