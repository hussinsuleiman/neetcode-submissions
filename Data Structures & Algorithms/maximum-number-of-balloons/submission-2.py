class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        occ = defaultdict(int)

        for c in text:
            occ[c] += 1
        
        print(occ)
        res = float('inf')

        if 'l' in occ:
            res = min(res, occ['l']//2)
        else:
            return 0
        
        if 'o' in occ:
            res = min(res, occ['o']//2)
        else:
            return 0

        for c in {'b','a','n'}:
            if c in occ:
                res = min(res, occ[c])
            else:
                return 0
    
        return res