class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        sums = set([0])
        tot = sum(stones)

        for s in stones:
            new = set()

            for x in sums:
                new.add(x)
                new.add(x+s)
            
            sums = new
        
        for i in range(sum(stones)//2, -1, -1):
            if i in sums:
                return tot - 2*i