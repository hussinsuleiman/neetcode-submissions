import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

for u in range(n):
    m, v = map(int, input().split())
    coins = [tuple(map(int, input().split())) for _ in range(m)]
    
    if u < n-1:
        input()
    
    vv = v*v
    dp = [[-1]*(v+1) for _ in range(v+1)]
    
    q = deque()
    q.append((0,0))
    dp[0][0] = 0
    answer = -1
    
    while q:
        x,y = q.popleft()
        
        for dx,dy in coins:
            nx = x + dx
            ny = y + dy
            
            if nx > v or ny > v:
                continue
                
            if nx*nx + ny*ny > vv:
                continue
            
            if dp[nx][ny] == -1:
                dp[nx][ny] = dp[x][y] + 1
                q.append((nx,ny))
                
                if nx*nx + ny*ny == vv:
                    answer = dp[nx][ny]
                    break
        
        if answer != -1:
            break
    
    if answer == -1:
        print("not possible")
    else:
        print(answer)