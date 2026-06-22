import math

n = int(input())
r = math.isqrt(n)

if r * r != n:
    print(0)
    exit()

m = r
tau = 1
d = 2

while d * d <= m:
    exp = 0
    
    while m % d == 0:
        m //= d
        exp += 1

    if exp > 0:
        tau *= exp + 1

    d += 1

if m > 1:
    tau *= 2

ans = tau // 2 - 1
print(max(0, ans))