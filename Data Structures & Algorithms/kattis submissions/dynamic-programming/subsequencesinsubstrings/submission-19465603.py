s = input()
t = input()
n,m = len(s), len(t)
dp = [-1]*m
res = 0

for i in range(n):
    for j in range(m-1, -1, -1):
        if s[i] == t[j]:
            if j == 0:
                dp[0] = i
            else:
                dp[j] = dp[j-1]
    
    if dp[m-1] != -1:
        res += dp[m-1]+1

print(res)