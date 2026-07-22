class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        l = len(prices)
        best = 0
        buy = float('inf')

        while i < l-1 and prices[i] >= prices[i+1]:
            i += 1

        while i < l:
            buy = min(buy, prices[i])
            
            while i < l-1 and prices[i] <= prices[i+1]:
                i += 1
            
            best = max(best, prices[i] - buy)
            i += 1
            
        return best   