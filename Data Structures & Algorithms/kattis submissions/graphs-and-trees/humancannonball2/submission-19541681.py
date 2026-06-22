from math import cos, sin, pi
N = int(input())

for _ in range(N):
    v0,theta,x1,h1,h2 = map(float, input().split())
    h1,h2 = h1+1, h2-1
    theta = theta/180*pi
    
    t = x1/(v0*cos(theta))
    y = v0*t*sin(theta) - 0.5*9.81*t**2
    
    if h1 <= y and y <= h2:
        print("Safe")
    else:
        print("Not Safe")