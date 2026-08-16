class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        res = 0
        dico = [0] * 26

        for c in chars:
            dico[ord(c) - ord('a')] += 1
        
        for w in words:
            occ = [0] * 26

            for c in w:
                occ[ord(c) - ord('a')] += 1
            
            valid = True

            for i in range(26):
                if occ[i] > dico[i]:
                    valid = False
                    break

            if valid:
                res += len(w)
        
        return res