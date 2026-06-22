n = int(input())

for _ in range(n):
    K,f = input().split()
    p,q = f.split('/')
    p,q = int(p), int(q)
    k = p//q
    p %= q
    q -= p
    p += q
    q += p*k
    print(K + ' ' + str(p) + '/' + str(q))