class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dico1 = dict()
        dico2 = dict()

        for i in range(len(s)):
            if s[i] in dico1.keys() and dico1[s[i]] != t[i]:
                return False
            if t[i] in dico2.keys() and dico2[t[i]] != s[i]:
                return False

            dico1[s[i]] = t[i]
            dico2[t[i]] = s[i]
        
        return True