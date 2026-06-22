class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        res = [0]

        for i in range(1, len(heights)):
            while res and heights[i] >= heights[res[-1]]:
                res.pop()
            res.append(i)
        
        return res