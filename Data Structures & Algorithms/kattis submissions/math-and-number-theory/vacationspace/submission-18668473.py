import sys
input = sys.stdin.readline

n = int(input())
nbs = list(map(int, input().split()))

if n == 1:
    print(1)
else:
    dico = dict()
    
    for i in range(1, n+1):
        dico[nbs[i-1]] = i
    
    nbs.sort()
    minDist = {i: 0 for i in range(1, n+1)}
    minDist[dico[nbs[0]]] = nbs[1] - nbs[0]
    minDist[dico[nbs[n-1]]] = nbs[n-1] - nbs[n-2]
    
    for i in range(2, n):
        minDist[dico[nbs[i-1]]] = min(nbs[i-1] - nbs[i-2], nbs[i] - nbs[i-1])
    
    res = max(minDist.values())
    
    for i in range(1, n+1):
        if minDist[i] == res:
            print(i)    
            break
    
    