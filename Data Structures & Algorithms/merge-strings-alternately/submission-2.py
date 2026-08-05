class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        new = []
        i,j = 0,0
        m,n = len(word1), len(word2)

        while i < m and j < n:
            new.append(word1[i])
            new.append(word2[j])
            i += 1
            j += 1
        
        if i == m:
            while j < n:
                new.append(word2[j])
                j += 1
        else:
            while i < m:
                new.append(word1[i])
                i += 1
        
        return ''.join(new)