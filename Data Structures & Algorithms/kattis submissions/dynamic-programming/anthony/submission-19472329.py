N,M = map(int, input().split())
dp = [[0]*(M+1) for i in range(N+1)]

for i in range(1, N+1):
    dp[i][0] = 1

p = [float(input()) for i in range(N+M-1)]

for k in range(2, N+M+1):
    for i in range(min(k-1, N), 0, -1):
        if k-i > M:
            break
        dp[i][k-i] = dp[i][k-i-1] * p[N+M-k] + dp[i-1][k-i] * (1-p[N+M-k])

print(dp[N][M])