import sys
input = sys.stdin.readline

T = int(input())

def find(u, parent):
    while u != parent[u]:
        u = parent[u]
    return u

def union(u, v, parent, size):
    p1 = find(u, parent)
    p2 = find(v, parent)
    
    if p1 == p2:
        return False
    
    if size[p1] < size[p2]:
        p1, p2 = p2, p1
    
    parent[p2] = p1
    size[p1] += size[p2]
    return True

for _ in range(T):
    M,C = map(int, input().split())
    weightEdges = []
    parent = {i: i for i in range(C)}
    size = {i: 1 for i in range(C)}
    
    for k in range(C*(C-1) // 2):
        i, j, D = map(int, input().split())
        weightEdges.append((D, i, j))
    
    weightEdges.sort()
    nbEdges = 0
    index = 0
    total = 0
    
    while nbEdges < C-1:
        D, i, j = weightEdges[index]
        
        if union(i, j, parent, size):
            total += D
            nbEdges += 1
        
        index += 1
    
    if total + C <= M:
        print("yes")
    else:
        print("no")