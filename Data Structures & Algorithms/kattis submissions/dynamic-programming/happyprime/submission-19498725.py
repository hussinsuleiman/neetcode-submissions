P = int(input())
memo = {1:" YES"}

isPrime = [True] * 10001
primes = []

for i in range(2, 10001):
    if isPrime[i]:
        primes.append(i)
    
    for p in primes:
        if p*i > 10000:
            break
        isPrime[p*i] = False
        
happy = set()

for p in primes:
    seen = set([p])
    nb = p
    
    while nb != 1:
        new = 0
        
        while nb != 0:
            new += (nb%10)**2
            nb //= 10
        
        nb = new
        
        if nb in seen:
            break
        
        seen.add(nb)
    
    if nb == 1:
        happy.add(p)

for i in range(1, P+1):
    K, m = map(int, input().split())
    
    if m in happy:
        print(str(K) + ' ' + str(m) + ' YES')
    else:
        print(str(K) + ' ' + str(m) + ' NO')