class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        dico = defaultdict(int)

        for elt in arr:
            dico[elt] += 1
        
        cnt = 0
        
        for elt in arr:
            if dico[elt] == 1:
                cnt += 1

                if cnt == k:
                    return elt
        
        return ''