class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        r = 0
        l1, l2 = len(g), len(s)
        i,j = 0,0

        while i < l1 and j < l2:
            if s[j] >= g[i]:
                r += 1
                i += 1
            j += 1
        
        return r