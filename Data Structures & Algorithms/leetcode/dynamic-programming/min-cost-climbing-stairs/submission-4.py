class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        minCost = cost

        for i in range(len(cost)-3, -1, -1):
            minCost[i] += min(cost[i+1], cost[i+2])
        
        return min(minCost[0], minCost[1])
