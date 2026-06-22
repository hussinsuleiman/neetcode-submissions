s = input()

while s != 'X':
    n = len(s)
    dp = [[0,0,0] for i in range(n+1)]
    
    for i in range(1, n+1):
        dp[i][0] = dp[i-1][0] if s[i-1] == 'A' else dp[i-1][2] + 2**(i-1) if s[i-1] == 'B' else dp[i-1][1] + 2**(i-1)
        dp[i][1] = dp[i-1][1] if s[i-1] == 'B' else dp[i-1][0] + 2**(i-1) if s[i-1] == 'C' else dp[i-1][2] + 2**(i-1)
        dp[i][2] = dp[i-1][2] if s[i-1] == 'C' else dp[i-1][1] + 2**(i-1) if s[i-1] == 'A' else dp[i-1][0] + 2**(i-1)
    
    print(dp[n][1])
    s = input()