def find(parent, u):
    while u != parent[u]:
        u = parent[u]
    return u

def union(u, v, parent, size):
    p1, p2 = find(parent, u), find(parent, v)
    
    if p1 == p2:
        return False
    
    if size[p1] < size[p2]:
        p1,p2 = p2,p1
    
    parent[p2] = p1
    size[p1] += size[p2]
    return True

n,m = map(int, input().split())
edges = []

for k in range(m):
    h1,h2,d = map(int, input().split())
    edges.append((d,h1,h2,k+1))

edges.sort()
chosen = []
nbChosen = 0
index = 0
parent = {i:i for i in range(1,n+1)}
size = {i:1 for i in range(1,n+1)}

while nbChosen < n-1:
    d,h1,h2,k = edges[index]
    
    if union(h1, h2, parent, size):
        chosen.append(str(k))
        nbChosen += 1
    
    index += 1

print(str(nbChosen))
print('\n'.join(chosen))