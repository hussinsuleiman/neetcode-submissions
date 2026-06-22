T = int(input())
primes = [2]

for i in range(3, 1000):
    for p in primes:
        if i % p == 0:
            continue
    primes.append(i)

for i in range(T):
    n, e = map(int, input().split())
    totient = 0
    
    for j in range(len(primes)):
        if n % primes[j] == 0:
            totient = (primes[j]-1) * (n // primes[j]-1)
            break
    
    nb = 1
    
    while nb % e != 0:
        nb += totient
    
    print(nb // e)
    
