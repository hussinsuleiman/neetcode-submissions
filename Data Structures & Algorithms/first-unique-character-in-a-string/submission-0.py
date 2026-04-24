class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = defaultdict(list)

        for i in range(len(s)):
            d[s[i]].append(i)
        
        m = len(s)

        for elt in d.keys():
            if len(d[elt]) == 1:
                m = min(m, d[elt][0])
        
        if m == len(s):
            return -1
        
        return m