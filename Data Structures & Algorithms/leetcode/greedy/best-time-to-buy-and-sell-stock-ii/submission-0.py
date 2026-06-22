class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total = 0
        l = len(prices)

        for i in range(l-1):
            total += max(0, prices[i+1] - prices[i])
        
        return total