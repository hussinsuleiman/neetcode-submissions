class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charsToInd = dict()
        i,j = 0,0
        res = 0
        n = len(s)

        while j < n:
            if s[j] in charsToInd:
                ind = charsToInd[s[j]]

                while i <= ind:
                    del charsToInd[s[i]]
                    i += 1
                
            charsToInd[s[j]] = j
            j += 1
            res = max(res, j-i)
        
        return res