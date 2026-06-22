import sys
input = sys.stdin.readline

def find(u, parent):
    while u != parent[u]:
        u = parent[u]
    return u

def union(u, v, parent, size):
    par1 = find(u, parent)
    par2 = find(v, parent)
    
    if par1 == par2:
        return False
    
    if size[par1] < size[par2]:
        par1, par2 = par2, par1

    parent[par2] = par1
    size[par1] += size[par2]
    return True

n, m, k = map(int, input().split())
weightEdges = []
weightEdges2 = []

for i in range(m):
    c, f, t = map(str, input().split())
    f, t = int(f), int(t)
    
    if c == 'B':
        weightEdges.append((1, f, t))
        weightEdges2.append((0, f, t))
    else:
        weightEdges.append((0, f, t))
        weightEdges2.append((1, f, t))

weightEdges.sort()
weightEdges2.sort()

parent = {i: i for i in range(1, n+1)}
size = {i: 1 for i in range(1, n+1)}
index = 0
minBlue = 0
nbEdges = 0

while nbEdges < n-1 and index < m:
    w, f, t = weightEdges[index]
    
    if union(f, t, parent, size):
        nbEdges += 1
        minBlue += w
        
    index += 1

parent = {i: i for i in range(1, n+1)}
size = {i: 1 for i in range(1, n+1)}
index = 0
maxBlue = 0
nbEdges = 0

while nbEdges < n-1 and index < m:
    w, f, t = weightEdges2[index]
    
    if union(f, t, parent, size):
        maxBlue += (1-w)
        nbEdges += 1
        
    index += 1

if minBlue <= k and k <= maxBlue:
    print(1)
else:
    print(0)