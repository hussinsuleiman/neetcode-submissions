import sys
from math import gcd

A = input()
L = len(A)
P, M = map(int, input().split())

res = []
cur = []

for c in A:
    if c != 'x':
        cur.append(c)
    else:
        res.append(''.join(cur))
        cur = []

res.append(''.join(cur))

coeff = [0, 0]

for mid in range(2):
    new = []

    for i in range(len(res) - 1):
        new.append(res[i] + str(mid))

    new.append(res[-1])
    new = ''.join(new)

    coeff[mid] = eval(new) % M

b = coeff[0]
a = (coeff[1] - coeff[0]) % M
c = (P - b) % M
g = gcd(a, M)

if c % g != 0:
    print(-1)
else:
    a //= g
    c //= g
    mod = M // g
    ans = (c * pow(a, -1, mod)) % mod
    print(ans)