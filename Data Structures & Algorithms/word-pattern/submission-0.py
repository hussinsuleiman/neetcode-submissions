class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(' ')
        dico = dict()

        if len(pattern) != len(words):
            return False

        for i,c in enumerate(pattern):
            if c in dico and dico[c] != words[i]:
                return False

            dico[c] = words[i]
        
        k = set()

        for c in dico:
            if dico[c] in k:
                return False
            k.add(dico[c])
        
        return True