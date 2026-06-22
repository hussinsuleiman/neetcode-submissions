import sys
sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline())
deps = {}          
rev = {}         

for _ in range(n):
    line = sys.stdin.readline().strip()
    left, right = line.split(":", 1)
    target = left
    dep_list = right.split()
    deps[target] = dep_list
    
    if target not in rev:
        rev[target] = []

    for d in dep_list:
        if d not in rev:
            rev[d] = []
            
        rev[d].append(target)

changed = sys.stdin.readline().strip()
affected = set()

def mark(u):
    if u in affected:
        return
    
    affected.add(u)
    
    for v in rev.get(u, []):
        mark(v)

mark(changed)
visited = set()
order = []

def topo(u):
    if u in visited:
        return
    
    visited.add(u)
    
    for d in deps[u]:
        if d in affected:
            topo(d)
            
    order.append(u)

for f in affected:
    topo(f)

print("\n".join(order))