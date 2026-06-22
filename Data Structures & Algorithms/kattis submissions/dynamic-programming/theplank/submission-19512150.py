n = int(input())
dp = [1,2,4]
i = 3

while i < n:
    dp.append(dp[-1] + dp[-2] + dp[-3])
    i += 1

print(dp[i-1])