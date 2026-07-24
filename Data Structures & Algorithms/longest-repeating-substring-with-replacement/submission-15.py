class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dico = dict()
        n = len(s)
        i, j = 0, 0
        m = 0
        res = 0

        while j < n:
            if s[j] in dico:
                dico[s[j]] += 1
            else:
                dico[s[j]] = 1
            
            m = max(m, dico[s[j]])
            j += 1

            if j-i > k+m:
                if dico[s[i]] > 1:
                    dico[s[i]] -= 1
                else:
                    del dico[s[i]]
                
                i += 1
            
            res = max(res, j-i)

        return res