class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        canBeJudge = [True] * n
        nbTrust = [0] * n

        for (i,j) in trust:
            canBeJudge[i-1] = False
            nbTrust[j-1] += 1
        
        for i in range(n):
            if canBeJudge[i] and nbTrust[i] == n-1:
                return i+1
        
        return -1