class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        i,j = 0,0
        nbWhite = 0
        res = k
        l = len(blocks)

        while j < k:
            if blocks[j] == 'W':
                nbWhite += 1
            j += 1
        
        while j < l:
            res = min(res, nbWhite)

            if blocks[j] == 'W':
                nbWhite += 1
            if blocks[i] == 'W':
                nbWhite -= 1
            
            i += 1
            j += 1

        return min(res, nbWhite)