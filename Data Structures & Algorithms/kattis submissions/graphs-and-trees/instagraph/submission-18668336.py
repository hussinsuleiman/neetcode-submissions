import sys
input = sys.stdin.readline

N,M = map(int, input().split())
adjList = {i: set() for i in range(1, N+1)}
followers = {i: set() for i in range(1, N+1)}

for i in range(M):
    u,v = map(int, input().split())
    adjList[u].add(v)
    followers[v].add(u)

maxCel = 0
maxIndex = 1

for i in range(1, N+1):
    cel = 0
    
    for nei in followers[i]:
        if nei not in adjList[i]:
            cel += 1
    
    if cel > maxCel:
        maxCel = cel
        maxIndex = i

print(maxIndex, maxCel)