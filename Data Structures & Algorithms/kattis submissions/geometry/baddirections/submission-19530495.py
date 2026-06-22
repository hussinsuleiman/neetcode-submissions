t = int(input())

for _ in range(t):
    k,n = input().split()
    l = len(n)
    nbs = [int(n[i]) for i in range(l)]
    k = int(k)
    
    for i in range(l):
        nbs[i] = str((nbs[i] + k)%10)
    
    print(''.join(nbs))