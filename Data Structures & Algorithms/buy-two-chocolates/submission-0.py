class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        t = min(prices)
        prices.remove(t)
        t += min(prices)
        return money-t if t <= money else money