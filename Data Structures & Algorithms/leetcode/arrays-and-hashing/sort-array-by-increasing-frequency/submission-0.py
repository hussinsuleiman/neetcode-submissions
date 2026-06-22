class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        occ = defaultdict(int)

        for n in nums:
            occ[n] += 1
        
        d = defaultdict(list)

        for n in occ.keys():
            d[occ[n]].append(n)

        for n in d.keys():
            d[n].sort()

        s = set(occ.values())
        out = []

        for elt in sorted(s):
            for i in range(len(d[elt])-1,-1,-1):
                for j in range(elt):
                    out.append(d[elt][i])
        
        return out
