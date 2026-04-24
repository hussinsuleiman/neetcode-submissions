class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        s1, s2 = sum(gas), sum(cost)
        n = len(gas)

        if s1 < s2:
            return -1
        
        ind = 0
        s, i = 0, 0

        while i < n:
            if s + gas[i] - cost[i] < 0:
                ind = i+1
                i = ind
                s = 0
            
            else:
                s += gas[i]-cost[i]
                i += 1

        return ind