from collections import deque

def to_coord(s):
    return ord(s[0]) - ord('a'), int(s[1]) - 1

def to_square(x, y):
    return chr(ord('a') + x) + str(y + 1)

start = input().strip()
target = input().strip()

sx, sy = to_coord(start)
tx, ty = to_coord(target)

moves = [(1, 2), (2, 1), (2, -1), (1, -2),(-1, -2), (-2, -1), (-2, 1), (-1, 2)]
neighbors = {}

for x in range(8):
    for y in range(8):
        nxt = []
        
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < 8 and 0 <= ny < 8:
                nxt.append((nx, ny))
                
        nxt.sort(key=lambda p: to_square(p[0], p[1]))
        neighbors[(x, y)] = nxt

INF = 10**9
dist = [[INF] * 8 for _ in range(8)]
dist[sx][sy] = 0
q = deque([(sx, sy)])

while q:
    x, y = q.popleft()
    
    for nx, ny in neighbors[(x, y)]:
        if dist[nx][ny] == INF:
            dist[nx][ny] = dist[x][y] + 1
            q.append((nx, ny))

best = dist[tx][ty]
path = [start]
ans = []

def dfs(x, y):
    if (x, y) == (tx, ty):
        ans.append(" -> ".join(path))
        return

    for nx, ny in neighbors[(x, y)]:
        if dist[nx][ny] == dist[x][y] + 1 and dist[nx][ny] <= best:
            path.append(to_square(nx, ny))
            dfs(nx, ny)
            path.pop()

dfs(sx, sy)

for line in ans:
    print(line)