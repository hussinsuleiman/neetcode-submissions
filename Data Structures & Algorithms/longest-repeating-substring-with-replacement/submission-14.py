class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dico = dict()
        n = len(s)
        i, j = 0, 0
        m = 0
        res = 0

        while j < n:
            if s[j] in dico:
                dico[s[j]].append(j)
            else:
                dico[s[j]] = [j]
            
            m = max(m, len(dico[s[j]]))
            j += 1

            if j-i > k+m:
                ind = dico[s[i]][0]

                if len(dico[s[i]]) > 1:
                    dico[s[i]] = dico[s[i]][1:]
                else:
                    del dico[s[i]]
                
                i = ind+1
            
            res = max(res, j-i)

        return res