import math

m,n,t,p = map(int, input().split())
r = (p+t-1)//t

def comb(n,k):
    return math.lgamma(n+1) - math.lgamma(k+1) - math.lgamma(n-k+1)

if r > n:
    print(0)
    exit()

if r <= n-(m-p):
    print(1)
    exit()

res = 0
C = comb(m,n)

for k in range(r, min(n,p)+1):
    cur = comb(p,k) + comb(m-p, n-k) - C
    res += math.exp(cur)

print(res)