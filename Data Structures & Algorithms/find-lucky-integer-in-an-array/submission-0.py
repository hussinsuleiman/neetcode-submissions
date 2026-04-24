class Solution:
    def findLucky(self, arr: List[int]) -> int:
        occ = defaultdict(int)

        for i in range(len(arr)):
            occ[arr[i]] += 1
        
        r = -1

        for elt in occ.keys():
            if occ[elt] == elt:
                r = max(r, elt)
        
        return r