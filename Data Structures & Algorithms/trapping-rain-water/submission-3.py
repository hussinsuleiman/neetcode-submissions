class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        pre = [0]*n
        suf = [0]*n

        for i in range(1,n):
            pre[i] = max(pre[i-1], height[i-1])
        
        for i in range(n-2, -1, -1):
            suf[i] = max(suf[i+1], height[i+1])
        
        area = 0

        for i in range(n):
            area += max(0, min(pre[i], suf[i]) - height[i])
        
        return area