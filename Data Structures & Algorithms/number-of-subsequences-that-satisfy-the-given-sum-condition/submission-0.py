class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        i,j = 0, len(nums)-1
        MOD = 10**9+7
        total = 0

        while i <= j:
            if nums[i] + nums[j] > target:
                j -= 1
            else:
                total = (total + 2**(j-i)) % MOD
                i += 1
        
        return total


