K = int(input())
nbs = list(map(int, input().split()))
parent = {}

while nbs != [-1]:
    for b in nbs[1:]:
        parent[b] = nbs[0]
    
    nbs = list(map(int, input().split()))

ans = [str(K)]

while K in parent:
    K = parent[K]
    ans.append(str(K))

print(' '.join(ans))