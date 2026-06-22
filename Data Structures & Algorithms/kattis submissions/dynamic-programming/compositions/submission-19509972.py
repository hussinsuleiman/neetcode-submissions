P = int(input())

for i in range(P):
    K,n,m,k = map(int, input().split())
    dp = [0]*(n+1)
    dp[0] = 1
    
    for i in range(1, n+1):
        for j in range(i-1, -1, -1):
            if (i-j)%k == m:
                continue
            dp[i] += dp[j]
    
    print(str(K) + ' ' + str(dp[-1]))