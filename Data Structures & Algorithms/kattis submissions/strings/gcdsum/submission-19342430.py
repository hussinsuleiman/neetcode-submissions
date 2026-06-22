N = int(input())
primes = []
exp = []
i = 2

while i*i <= N:
    e = 0
    
    while N%i == 0:
        N //= i
        e += 1
    
    if e > 0:
        primes.append(i)
        exp.append(e)
    
    i += 1

if N > 1:
    primes.append(N)
    exp.append(1)

l = len(primes)
res = 1

for i in range(l):
    s = 0
    a = exp[i]
    p = primes[i]
    
    for t in range(a+1):
        s += p**t * (2*(a-t)+1)
    
    res *= s

print(res)