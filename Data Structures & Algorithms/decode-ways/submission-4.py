class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [1]*(n+1)

        if s[0] == '0':
            return 0
        
        dp[1] = 1
        
        for i in range(1, n):
            if s[i] == '0':
                if s[i-1] in {'1','2'}:
                    dp[i+1] = dp[i-1]
                else:
                    return 0

            elif s[i] not in {'1', '2'}:
                if s[i] in {'3','4','5','6'}:
                    if s[i-1] in {'1','2'}:
                        dp[i+1] = dp[i-1] + dp[i]
                    else:
                        dp[i+1] = dp[i]
                
                elif s[i-1] == '1':
                    dp[i+1] = dp[i-1] + dp[i]

                else:
                    dp[i+1] = dp[i]
            
            elif s[i-1] not in {'1', '2'}:
                dp[i+1] = dp[i]
            
            else:
                dp[i+1] = dp[i-1] + dp[i]
        
        return dp[n]