class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        res = 0

        for w in words:
            valid = True

            for c in w:
                if c not in allowed:
                    valid = False
                    break
            
            if valid:
                res += 1
        
        return res