N = int(input())
adjList = [[] for i in range(N)]

for i in range(N):
    nbs = list(map(int, input().split()))
    adjList[i] = nbs

color = [-1] * N
best = N

def can_color(v,c):
    for nei in adjList[v]:
        if color[nei] == c:
            return False
    return True

def dfs(v, used_colors):
    global best
    
    if used_colors >= best:
        return
    
    if v == N:
        best = used_colors
        return
    
    for c in range(used_colors):
        if can_color(v, c):
            color[v] = c
            dfs(v+1, used_colors)
            color[v] = -1
    
    color[v] = used_colors
    dfs(v+1, used_colors+1)
    color[v] = -1

dfs(0,0)
print(best)