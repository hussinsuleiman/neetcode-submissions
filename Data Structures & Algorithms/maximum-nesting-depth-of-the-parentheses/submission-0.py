class Solution:
    def maxDepth(self, s: str) -> int:
        cnt = 0
        res = 0

        for elt in s:
            if elt == '(':
                cnt += 1
            
            elif elt == ')':
                res = max(res, cnt)
                cnt -= 1
        
        return max(res, cnt)