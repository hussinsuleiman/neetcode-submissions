class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        i,j = 0,n-1
        res = 0

        while i < j:
            if heights[i] <= heights[j]:
                res = max(res, heights[i] * (j-i))
                i += 1
            else:
                res = max(res, heights[j] * (j-i))
                j -= 1
        
        return res