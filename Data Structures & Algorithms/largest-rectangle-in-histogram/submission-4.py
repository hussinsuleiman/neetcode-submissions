class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []
        res = 0

        for i,h in enumerate(heights):
            idx = i

            while stack and h < stack[-1][1]:
                res = max(res, (i-stack[-1][0]) * stack[-1][1])
                idx = stack[-1][0]
                stack.pop()

            stack.append((idx,h))

        while stack:
            res = max(res, (n-stack[-1][0]) * stack[-1][1])
            stack.pop()

        return res