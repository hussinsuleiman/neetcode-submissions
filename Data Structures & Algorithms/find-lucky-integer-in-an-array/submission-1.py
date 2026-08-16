class Solution:
    def findLucky(self, arr: List[int]) -> int:
        best = -1
        dico = defaultdict(int)

        for n in arr:
            dico[n] += 1
        
        for n in dico:
            if dico[n] == n:
                best = max(best, n)
        
        return best