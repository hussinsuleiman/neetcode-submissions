class Solution:
    def maxDifference(self, s: str) -> int:
        occ = defaultdict(int)

        for c in s:
            occ[c] += 1
        
        f1, f2 = 0, float('inf')

        for c in occ:
            if occ[c]%2 == 1:
                f1 = max(f1, occ[c])
            else:
                f2 = min(f2, occ[c])
        
        return f1 - f2