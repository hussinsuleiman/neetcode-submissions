class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights)-1
        areaMax = 0

        while i < j:
            area = 0

            if heights[i] < heights[j]:    
                area = heights[i] * (j-i)
                i += 1
            else:
                area = heights[j] * (j-i)
                j -= 1

            if area > areaMax:
                areaMax = area
            
        return areaMax
