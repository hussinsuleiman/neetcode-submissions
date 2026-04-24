class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        areaMax = 0
        n = len(heights)
        stack = [(heights[0],0)]
    
        for i in range(n):
            if heights[i] <= stack[-1][0]:
                last_index = 0
                while len(stack) > 0 and heights[i] <= stack[-1][0]:
                    h, index = stack.pop()
                    areaMax = max(areaMax, h * (i-index))
                    last_index = index
                stack.append((heights[i], last_index))
            else:
                stack.append((heights[i], i))
        
        while len(stack) > 0:
            h, index = stack.pop()
            areaMax = max(areaMax, h * (n-index))
        
        return areaMax