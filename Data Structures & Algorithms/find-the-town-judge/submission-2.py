class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        diff = [0] * n

        for a,b in trust:
            diff[a-1] -= 1
            diff[b-1] += 1
        
        for elt in range(n):
            if diff[elt] == n-1:
                return elt+1

        return -1