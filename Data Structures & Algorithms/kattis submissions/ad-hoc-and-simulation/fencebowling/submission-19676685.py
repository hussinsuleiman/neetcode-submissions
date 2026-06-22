from math import atan, pi

k,w,l = map(int, input().split())
x = l/(2**(k+2)-2**k-3)
print(atan(2*x/w)*180/pi)