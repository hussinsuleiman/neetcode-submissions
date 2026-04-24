class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        l = len(days)
        dp = [0 for i in range(l+1)]

        for i in range(l-1, -1, -1):
            dp[i] = dp[i+1] + costs[0]
            j = i

            while j < l and days[j]-days[i] < 7:
                j += 1

            dp[i] = min(dp[i], dp[j] + costs[1])

            while j < l and days[j]-days[i] < 30:
                j += 1

            dp[i] = min(dp[i], dp[j] + costs[2])
            
        return dp[0]  