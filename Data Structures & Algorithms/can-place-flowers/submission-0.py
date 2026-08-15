class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        m = 0
        i = 0
        l = len(flowerbed)

        while i < l:
            if flowerbed[i] == 1:
                i += 2
            elif i == l-1 or flowerbed[i+1] == 0:
                m += 1
                i += 2
            else:
                i += 1

        return m >= n