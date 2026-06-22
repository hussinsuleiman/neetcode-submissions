import sys
input = sys.stdin.readline

def gcd(a,b):    
    while a != b:
        if a == 0:
            return b
        if b == 0:
            return a
        
        if a > b:
            q = a // b
            a -= b*q
        else:
            q = b // a
            b -= a*q
            
    return a
    
def lcm(a, b):
    return a*b // gcd(a,b)

A, B, C, D = map(int, input().split())
L = lcm(C, D)

first = A // L
if A%L > 0:
    first += 1

second = B // L
print(second-first+1)

