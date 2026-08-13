class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = [0]
        n = len(nums)
        cur = [0]

        def backtrack(i):
            if i == n:
                res[0] += cur[0]
                return
            
            temp = cur[0]
            cur[0] = cur[0] ^ nums[i]
            backtrack(i+1)
            cur[0] = temp
            backtrack(i+1)
        
        backtrack(0)
        return res[0]