class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        t = [0,0,0]

        for a,b,c in triplets:
            if a <= target[0] and b <= target[1] and c <= target[2]:
                t = [max(a,t[0]),max(b,t[1]),max(c,t[2])]
        
        return t == target