import sys
from collections import deque

def bfs(author, adjLists):
    queue = deque()
    queue.append(author)
    visited = set()
    level = 0
    dist = dict()
    visited.add(author)
    
    while queue:
        l = len(queue)
        
        for i in range(l):
            cur = queue.popleft()
            dist[cur] = level
            
            for neighbor in adjLists[cur]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)
                    
        level += 1
        
    return dist
    
authors = []
adjLists = dict()

for line in sys.stdin:
    if line == '\n':
        break
    
    inp = line.strip().split()
    authors.append(inp[0])
    l = len(inp)
    
    if inp[0] not in adjLists.keys():
        adjLists[inp[0]] = []
    
    for i in range(1, l):
        adjLists[inp[0]].append(inp[i])
        
        if inp[i] in adjLists.keys():
            adjLists[inp[i]].append(inp[0])
        else:
            adjLists[inp[i]] = [inp[0]]
    
distances = bfs("PAUL_ERDOS", adjLists)

for author in authors:
    if author in distances.keys():
        print(author + " " + str(distances[author]))
    else:
        print(author + " no-connection")