from math import sin, acos,cos

N = int(input())
tot = 0

for _ in range(N):
    A,B,C = map(int, input().split())
    theta = acos((C**2+A**2-B**2)/(2*A*C))
    h = (A**2 + C**2/4 - A*C*cos(theta))**0.5
    tot += A*C*sin(theta)/h

print(tot)