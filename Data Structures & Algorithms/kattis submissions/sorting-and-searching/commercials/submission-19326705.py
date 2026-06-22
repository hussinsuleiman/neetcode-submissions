N,P = map(int, input().split())
nbs = list(map(int, input().split()))

for i in range(N):
    nbs[i] -= P

res = 0
s = 0
nbElts = 0
maxElts = 0

for i in range(N):
    if s + nbs[i] <= 0:
        if s > res:
            res = s
            maxElts = nbElts
        
        s = 0
        nbElts = 0
    
    else:
        s += nbs[i]
        nbElts += 1
    
    res = max(res, s)

print(res + maxElts*P)