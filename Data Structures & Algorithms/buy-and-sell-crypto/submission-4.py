class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = len(prices)

        if l == 1:
            return 0

        i = 0
        j = 1
        profit = 0

        while j < l:
            if prices[i] > prices[j]:
                i = j
            else:
                profit = max(profit, prices[j]-prices[i])
                j += 1
        
        return profit
    