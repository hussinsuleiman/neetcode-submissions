class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start = 0
        diff = gas[0] - cost[0]
        n = len(gas)
        i = 1%n
        
        while True:
            while start != i and diff >= 0:
                diff += gas[i] - cost[i]
                i = (i+1)%n
            
            if start == i:
                return start if diff >= 0 else -1
            
            if i < start:
                break
            
            start = i
            diff = gas[i] - cost[i]
            i = (start+1)%n
            
        return -1