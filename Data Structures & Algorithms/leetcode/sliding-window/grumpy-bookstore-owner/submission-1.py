class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        indexGrumpy = []
        n = len(grumpy)
        total = 0

        for i in range(n):
            if grumpy[i] == 0:
                total += customers[i]
            else:
                indexGrumpy.append(i)
        
        i,j = 0,0
        l = len(indexGrumpy)
        cur = 0
        curMax = 0

        while j < l:
            while j < l and indexGrumpy[j]-indexGrumpy[i] < minutes:
                cur += customers[indexGrumpy[j]]
                j += 1

            curMax = max(curMax, cur)
            cur -= customers[indexGrumpy[i]]
            i += 1
        
        return curMax + total
