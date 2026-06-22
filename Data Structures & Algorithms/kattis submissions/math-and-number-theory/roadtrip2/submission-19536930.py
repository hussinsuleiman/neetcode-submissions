from collections import defaultdict

N,size,H,M,S = map(int, input().split())
cities = []
last = [-1] * N
adjList = defaultdict(list)

for _ in range(N):
    i,s,t = input().split()
    i,t = int(i), int(t)
    cities.append((i,s,t))

for _ in range(size):
    fr,to,d = map(int, input().split())
    adjList[fr].append((d,to))
    adjList[to].append((d,fr))

for key in adjList:
    adjList[key].sort()

T = cities[S][2]
ans = [cities[S][1]]
last[S] = T

while True:
    if S not in adjList:
        break
    
    best = -1
    minD = 0
    
    for d,i in adjList[S]:
        if T + d + cities[i][2] > M or (last[i] != -1 and T + d - last[i] < H):
            continue
        
        best = i
        minD = d
        break
    
    if best == -1:
        break
    
    S = i
    T += minD + cities[i][2]
    last[i] = T
    ans.append(cities[S][1])
        
print(' '.join(ans))
print(T)