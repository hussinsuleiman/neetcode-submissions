from collections import defaultdict

def dfs(cur, adjList, fav, memo):
    if cur in memo:
        return memo[cur]
    
    total = 0
    
    for nei in adjList[cur]:
        total += dfs(nei, adjList, fav, memo)
    
    memo[cur] = total        
    return total

T = int(input())

for i in range(T):
    S = int(input())
    adjList = defaultdict(list)
    fav = set()
    memo = {}
    
    for j in range(S):
        line = input().split()
        nb = int(line[0])
        
        if len(line) == 2 and line[1] == 'favourably':
            fav.add(nb)
            memo[nb] = 1
        
        elif len(line) == 2 and line[1] == 'catastrophically':
            memo[nb] = 0
        
        elif len(line) == 4:
            a,b,c = int(line[1]), int(line[2]), int(line[3])
            adjList[nb].append(a)
            adjList[nb].append(b)
            adjList[nb].append(c)
    
    res = dfs(1, adjList, fav, memo)
    print(res)