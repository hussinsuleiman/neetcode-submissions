class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [cost[0], cost[1]]

        for i in range(2, n):
            dp.append(min(dp[-2], dp[-1]) + cost[i])
        
        return min(dp[-1], dp[-2])