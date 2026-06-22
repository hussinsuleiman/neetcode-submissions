import heapq
import sys
input = sys.stdin.readline

def dist(a,b,c,d):
    return ((a-c)**2 + (b-d)**2)**0.5

Xstart, Ystart = map(float, input().split())
Xend, Yend = map(float, input().split())
n = int(input())
points = [(Xstart, Ystart)]

for i in range(n):
    X, Y = map(float, input().split())
    points.append((X, Y))

points.append((Xend, Yend))
times = [[0]*(n+2) for i in range(n+2)]

for i in range(n+2):
    x,y = points[i]
    times[0][i] = dist(Xstart, Ystart, x, y)/5

for i in range(1, n+1):
    a,b = points[i]
    
    for j in range(n+2):
        c,d = points[j]
        l = dist(a,b,c,d)
        times[i][j] = min(l/5, abs(50-l)/5 + 2)

for i in range(n+2):
    x,y = points[i]
    times[n+1][i] = dist(Xend, Yend, x, y)/5

INF = float('inf')
dp = [INF] * (n+2)
queue = [(0,0)]

while queue:
    time, cur = heapq.heappop(queue)
    
    if time > dp[cur]:
        continue
    
    dp[cur] = time
    
    for i in range(n+2):        
        if dp[i] > time + times[cur][i]:
            dp[i] = time + times[cur][i]
            heapq.heappush(queue, (dp[i], i))
                    
print(dp[n+1])