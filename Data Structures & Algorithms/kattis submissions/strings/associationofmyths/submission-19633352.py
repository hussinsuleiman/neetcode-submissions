from math import pi, e

a,b,c = map(float, input().split())
t1, t2, t3, t4 = map(int, input().split())
n,k,r,s,l = map(int, input().split())

print(l**2/(pi*e) + 1/(l+1))