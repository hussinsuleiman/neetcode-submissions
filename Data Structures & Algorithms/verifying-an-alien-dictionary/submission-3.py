class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dico = dict()
        n = len(words)

        for i in range(26):
            dico[order[i]] = i
        
        for i in range(n-1):
            l1, l2 = len(words[i]), len(words[i+1])
            valid = False
            m = min(l1, l2)

            for j in range(m):
                if dico[words[i][j]] < dico[words[i+1][j]]:
                    valid = True
                    break
                
                elif dico[words[i][j]] > dico[words[i+1][j]]:
                    return False
            
            if not valid and l1 <= l2:
                valid = True
            
            if not valid:
                return False
        
        return True