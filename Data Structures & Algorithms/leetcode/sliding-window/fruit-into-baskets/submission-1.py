class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        elts = dict()
        i,j = 0,0
        l = len(fruits)
        res = 0

        while j < l:
            if fruits[j] not in elts:
                if len(elts) == 2:
                    res = max(res, j-i)
                    k = l

                    for key in elts:
                        if k not in elts or elts[key] < elts[k]:
                            k = key
                    
                    i = elts[k]+1
                    del elts[k]
                
            elts[fruits[j]] = j
            j += 1
        
        return max(res, j-i)