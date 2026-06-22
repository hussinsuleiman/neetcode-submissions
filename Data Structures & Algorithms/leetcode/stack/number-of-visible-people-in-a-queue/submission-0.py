class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n = len(heights)
        ans = [0] * n
        cur = [heights[-1]]

        for i in range(n-2, -1, -1):
            val = 0

            while cur and heights[i] > cur[-1]:
                cur.pop()
                val += 1
            
            if cur:
                val += 1

            ans[i] = val
            cur.append(heights[i])
        
        return ans