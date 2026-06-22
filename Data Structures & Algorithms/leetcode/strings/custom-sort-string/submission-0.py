class Solution:
    def customSortString(self, order: str, s: str) -> str:
        occ = defaultdict(int)
        elts = set(order)

        for i in s:
            occ[i] += 1
        
        out = []

        for i in order:
            for j in range(occ[i]):
                out.append(i)
        
        for i in s:
            if i not in elts:
                out.append(i)
        
        return ''.join(out)
