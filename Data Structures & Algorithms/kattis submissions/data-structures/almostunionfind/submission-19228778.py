import sys
input = sys.stdin.readline

def find(u, parent):
    if parent[u] != u:
        parent[u] = find(parent[u], parent)
    return parent[u]

def union(u, v, parent, size, sums):
    p1, p2 = find(u, parent), find(v, parent)
    
    if p1 == p2:
        return
    
    if size[p1] < size[p2]:
        p1, p2 = p2, p1
    
    sums[p1] += sums[p2]
    parent[p2] = p1
    size[p1] += size[p2]

while True:
    line = input()
    if not line:
        break
    n,m = map(int, line.split())
    
    size = [1] * (n+m+1)
    sums = list(range(n+m+1))
    parent = list(range(n+m+1))
    next_id = n+1
    loc = list(range(n+1))
    
    for _ in range(m):
        cmd = input().split()
        
        if cmd[0] == '1':
            p, q = int(cmd[1]), int(cmd[2])
            union(loc[p], loc[q], parent, size, sums)
        
        elif cmd[0] == '2':
            p, q = int(cmd[1]), int(cmd[2])
            root_p, root_q = find(loc[p], parent), find(loc[q], parent)
            
            if root_p != root_q:
                size[root_p] -= 1
                sums[root_p] -= p
                
                loc[p] = new_node = next_id
                next_id += 1
                sums[new_node] = p
                parent[new_node] = new_node
                size[new_node] = 1
            
                union(new_node, root_q, parent, size, sums)
        
        else:
            p = int(cmd[1])
            root_p = find(loc[p], parent)
            print(size[root_p], sums[root_p])