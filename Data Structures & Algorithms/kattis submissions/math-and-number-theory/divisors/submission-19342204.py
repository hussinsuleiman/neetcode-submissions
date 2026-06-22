import sys

isPrime = [True] * 432
primes = []

for i in range(2, 432):
    if isPrime[i]:
        primes.append(i)
        
        for j in range(i*i, 432, i):
            isPrime[j] = False
    
def vp(n, p):
    s = 0
    
    while n > 1:
        n //= p
        s += n
    
    return s

for line in sys.stdin:
    n,k = map(int, line.split())
    res = 1
    
    for p in primes:
        if p > n:
            break
        
        e = vp(n, p) - vp(k, p) - vp(n-k, p)
        res *= (e+1)
    
    print(res)