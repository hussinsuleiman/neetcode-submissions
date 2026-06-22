import sys
from collections import deque
input = sys.stdin.readline

x, y = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(y)]

comp = [[-1] * x for _ in range(y)]
sizes = []
bad = []
dirs = [(1,0), (-1,0), (0,1), (0,-1)]
cid = 0

for i in range(y):
    for j in range(x):
        if comp[i][j] != -1:
            continue
        
        q = deque([(i, j)])
        comp[i][j] = cid
        cells = [(i, j)]
        ok = True

        while q:
            r, c = q.popleft()
            
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < y and 0 <= nc < x:
                    if g[nr][nc] == g[r][c] and comp[nr][nc] == -1:
                        comp[nr][nc] = cid
                        q.append((nr, nc))
                        cells.append((nr, nc))
                        
                    elif g[nr][nc] < g[r][c]:
                        ok = False

        sizes.append(len(cells))
        bad.append(not ok)
        cid += 1

print(sum(sizes[c] for c in range(cid) if not bad[c]))