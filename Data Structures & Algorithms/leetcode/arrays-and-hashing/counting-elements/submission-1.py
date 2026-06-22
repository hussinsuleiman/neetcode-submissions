class Solution:
    def countElements(self, arr: List[int]) -> int:
        occ = defaultdict(int)
        
        for elt in arr:
            occ[elt] += 1

        s = occ.keys()
        t = 0

        for elt in s:
            if elt+1 in s:
                t += occ[elt]
        
        return t