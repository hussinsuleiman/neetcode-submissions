class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        i,j = 0,0
        indZero = []
        n = len(nums)
        nbOnes = 0

        while j < n:
            if nums[j] == 0:
                if indZero:
                    nbOnes = max(nbOnes, j-i)
                    i = indZero[0]+1
                else:
                    indZero.append(j)
            
            j += 1
        
        return max(nbOnes, j-i)