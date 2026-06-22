import math

def egcd(a, b):
    if b == 0:
        return a, 1, 0
    
    g, x1, y1 = egcd(b, a % b)
    return g, y1, x1 - (a // b) * y1

def crt(a, n, b, m):
    g, x, y = egcd(n, m)

    if (b - a) % g != 0:
        return "no solution"

    n1 = n // g
    m1 = m // g
    t = ((b - a) // g * (x % m1)) % m1
    x0 = a + n * t
    mod = n * m1  

    return str(x0 % mod) + ' ' + str(mod)

T = int(input())

for i in range(T):
    a,n,b,m = map(int, input().split())
    print(crt(a,n,b,m))