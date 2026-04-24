class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        occ = defaultdict(int)

        for c in magazine:
            occ[c] += 1
        
        for c in ransomNote:
            if c not in occ.keys() or occ[c] == 0:
                return False
            
            occ[c] -= 1
        
        return True