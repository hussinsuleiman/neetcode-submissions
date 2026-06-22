import sys
input = sys.stdin.readline

N = int(input())
dp = []

for i in range(N+1):
    dp.append([0, 0, 0, 0, 0, 0])

den = [1, 5, 15, 30, 150]

for i in range(1, N+1):
    curTotal = float("inf")
    
    for j in range(5):
        if i-den[j] >= 0 and dp[i-den[j]][-1] + 1 < curTotal:
            curTotal = dp[i-den[j]][-1] + 1
            dp[i] = dp[i-den[j]].copy()
            dp[i][-1] = curTotal
            dp[i][j] += 1

output = []
index = 0

for elt in dp[N]:
    if index < 5:
        output.append(str(elt))
    index += 1

print(" ".join(output))
    


