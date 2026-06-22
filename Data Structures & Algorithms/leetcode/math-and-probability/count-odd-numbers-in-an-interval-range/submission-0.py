class Solution:
    def countOdds(self, low: int, high: int) -> int:
        lower = low // 2
        upper = high // 2 

        if high%2 == 0:
            upper -= 1

        return upper - lower + 1
