M = int(input())
N = int(input())
dp = [0]*(M+1)
dp[0] = 1
times = [int(input()) for i in range(N)]
times.sort()

for i in range(1, M+1):
    for t in times:
        if t > i:
            break
        dp[i] += dp[i-t]

print(dp[-1])