n, k = map(int, input().split())
q = n // k
r = n % k

if n < k:
    print(n)
    
elif r == 0:
    print(k)
    
else:
    res = (k-r) // (q+1)
    
    if (k-r) % (q+1) != 0:
        res += 1
    
    print(k - res)