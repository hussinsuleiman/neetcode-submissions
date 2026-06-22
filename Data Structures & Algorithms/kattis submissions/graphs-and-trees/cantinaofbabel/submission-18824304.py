def dfs(name, adjList):
    stack = [name]
    visited = set()
    
    while stack:
        cur = stack.pop()
        visited.add(cur)
        
        for elt in adjList[cur]:
            if elt not in visited:
                stack.append(elt)
    
    return visited

N = int(input())
languages = dict()
adjList = dict()
adjListReverse = dict()

for i in range(N):
    line = input().split()
    name = line[0]
    languages[name] = (line[1], set(line[2:]))
    adjacent = []
    adjacentRev = []
    
    for nei in adjList.keys():
        if languages[nei][0] == languages[name][0]:
            adjacent.append(nei)
            adjList[nei].append(name)
            adjacentRev.append(nei)
            adjListReverse[nei].append(name)
            
        else:
            if languages[nei][0] in languages[name][1]:
                adjList[nei].append(name)
                adjacentRev.append(nei)
        
            if languages[name][0] in languages[nei][1]:
                adjacent.append(nei)
                adjListReverse[nei].append(name)
    
    adjList[name] = adjacent
    adjListReverse[name] = adjacentRev  

maxResult = 0

for name in adjList.keys():
    canTalkTo = dfs(name, adjList)
    canUnderstand = dfs(name, adjListReverse)
    result = 0
    
    for elt in canTalkTo:
        if elt in canUnderstand:
            result += 1
    
    if result > maxResult:
        maxResult = result

print(N - maxResult)