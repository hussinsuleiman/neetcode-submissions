n = int(input())
INF = float('inf')
dp = [INF] * n
prev = [-1] * n
dp[0] = 0

for i in range(1, n):
    cost = list(map(int, input().split()))
    
    for j in range(i+1, n+1):
        if dp[j-1] > dp[i-1] + cost[j-i-1]:
            dp[j-1] = dp[i-1] + cost[j-i-1]
            prev[j-1] = i-1

sol = []
cur = n-1

while cur != -1:
    sol.append(str(cur+1))
    cur = prev[cur]

sol = sol[::-1]
print(' '.join(sol))
print(dp[-1])