class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = len(weights)
        
        def nbDays(m):
            index = 0
            output = 0

            while index < l:
                s = 0

                while s < m and index < l:
                    s += weights[index]
                    index += 1
            
                if s > m:
                    index -= 1
                
                output += 1

            return output
        
        maxi = 0
        sumNbs = 0

        for w in weights:
            sumNbs += w
            
            if w > maxi:
                maxi = w

        i, j = maxi, sumNbs

        while i < j:
            m = (i+j) // 2
            k = nbDays(m)

            if k <= days:
                j = m-1
            else:
                i = m+1
        
        k = nbDays(i)

        if k <= days:
            return i
        else:
            return i+1
