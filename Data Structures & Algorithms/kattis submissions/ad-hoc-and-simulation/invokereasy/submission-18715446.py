import sys
input = sys.stdin.readline

a,b = map(int, input().split())
c,d = map(int, input().split())

real = (a*c + b*d)  / (c**2 + d**2)
imaginary = (-a*d + b*c) / (c**2 + d**2)

print(real, imaginary)