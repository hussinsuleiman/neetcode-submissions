from math import pi, acos

n = int(input())

for _ in range(n):
    D,d,s = map(float, input().split())
    alpha = acos(1 - 2*(s+d)**2/((D-d)**2))
    print(int(2*pi/alpha))