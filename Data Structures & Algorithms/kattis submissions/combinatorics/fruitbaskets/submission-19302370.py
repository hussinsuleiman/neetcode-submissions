N = int(input())
nbs = list(map(int, input().split()))
res = 0

for i in range(N):
    if nbs[i] >= 200:
        res += nbs[i]
    
    for j in range(i+1, N):
        if nbs[i] + nbs[j] >= 200:
            res += nbs[i] + nbs[j]
        
        for k in range(j+1, N):
            if nbs[i] + nbs[j] + nbs[k] >= 200:
                res += nbs[i] + nbs[j] + nbs[k]

if N >= 4:
    s = sum(nbs)
    res += s * (2**(N-1) - N - (N-1)*(N-2)//2)

print(res)