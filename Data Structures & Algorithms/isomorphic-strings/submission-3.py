class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        dico = dict()

        for i in range(len(s)):
            if s[i] in dico and dico[s[i]] != t[i]:
                return False
            dico[s[i]] = t[i]
        
        k = set()

        for c in dico:
            if dico[c] in k:
                return False
            k.add(dico[c])
        
        return True
                