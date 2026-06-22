P = int(input())
sums = [0]

for b in range(1, 10001):
    primes = []
    p = 2
    totient = b
    
    while p*p <= b:
        if b%p == 0:
            primes.append(p)
            
            while b%p == 0:
                b //= p
        
        p += 1
    
    if b > 1:
        primes.append(b)
    
    for p in primes:
        totient = totient - totient//p
    
    sums.append(sums[-1] + totient)
    
for i in range(P):
    K,N = map(int, input().split())
    res = 1 + sums[N]
    print(str(K) + ' ' + str(res))