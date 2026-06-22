from collections import defaultdict

s = input()
N = len(s)
occ = defaultdict(int)

for c in s:
    occ[c] += 1

if len(occ.keys()) == 1:
    print(-1)
    exit()

m = N+1
best = ''

for c in occ:
    if occ[c] < m:
        best = c
        m = occ[c]

res = [''] * N

for i in range(N//2-1, N//2-1+m):
    res[i] = best

index = 0

for c in occ:
    if c == best:
        continue
    
    while occ[c] > 0 and index < N//2-1:
        res[index] = c
        occ[c] -= 1
        index += 1

index = N//2-1+m

for c in occ:
    if c == best:
        continue
    
    while occ[c] > 0:
        res[index] = c
        occ[c] -= 1
        index += 1

print(''.join(res))