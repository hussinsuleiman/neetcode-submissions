from collections import defaultdict

N,M = map(int, input().split())
adjList = defaultdict(list)

for i in range(M):
    a,b = map(int, input().split())
    adjList[a].append(b)
    adjList[b].append(a)

seen = set([1])
stack = [1]

while stack:
    cur = stack.pop()
    
    for nei in adjList[cur]:
        if nei not in seen:
            stack.append(nei)
            seen.add(nei)

con = True

for i in range(1, N+1):
    if i not in seen:
        print(i)
        con = False

if con:
    print("Connected")