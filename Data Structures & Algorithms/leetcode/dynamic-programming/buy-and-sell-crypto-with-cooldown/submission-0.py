class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = len(prices)
        dp = [0] * l

        for i in range(l-2, -1, -1):
            m = dp[i+1]

            for j in range(i+1, l):
                cur = prices[j]-prices[i]

                if j < l-2:
                    cur += dp[j+2]
                
                m = max(cur, m)
            
            dp[i] = m
        
        return dp[0]