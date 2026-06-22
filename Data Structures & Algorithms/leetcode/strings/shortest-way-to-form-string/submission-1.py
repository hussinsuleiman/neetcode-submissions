class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        if target == '':
            return 0
        
        l = len(source)
        t = len(target)
        i,j = 0,0

        while i < l and j < t:
            while i < l and source[i] != target[j]:
                i += 1
            
            if i == l:
                if j == 0:
                    return -1
                break

            i += 1
            j += 1
        
        prev = self.shortestWay(source, target[j:])

        if prev == -1:
            return prev

        return 1 + prev