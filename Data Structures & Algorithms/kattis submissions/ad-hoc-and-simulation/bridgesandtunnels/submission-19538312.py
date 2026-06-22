n = int(input())
parent = {}
size = {}

def find(parent, a):
    while a != parent[a]:
        a = parent[a]
    return a

def union(parent, size, a, b):
    p,q = find(parent, a), find(parent, b)
    
    if p == q:
        return p
    
    if size[p] < size[q]:
        p,q = q,p
    
    size[p] += size[q]
    parent[q] = p
    return p

for _ in range(n):
    a,b = input().split()
    
    if a not in parent:
        parent[a] = a
        size[a] = 1
    
    if b not in parent:
        parent[b] = b
        size[b] = 1
    
    r = union(parent, size, a, b)
    print(size[r])