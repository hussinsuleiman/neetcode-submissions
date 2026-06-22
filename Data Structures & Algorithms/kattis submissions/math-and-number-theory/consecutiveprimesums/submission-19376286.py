n = int(input())

isPrime = [True] * (n)
primes = []

for i in range(2, n):
    if isPrime[i]:
        primes.append(i)
        
    for p in primes:
        if p*i >= n:
            break
        isPrime[p*i] = False

pre = [0]
l = len(primes)
done = False

for i in range(l):
    pre.append(pre[-1] + primes[i])

for j in range(l, 0, -1):
    for k in range(l+1-j):
        if pre[k+j] - pre[k] >= n:
            break
        
        if isPrime[pre[k+j] - pre[k]]:
            print(pre[k+j] - pre[k])
            done = True
            break
            
    if done:
        break