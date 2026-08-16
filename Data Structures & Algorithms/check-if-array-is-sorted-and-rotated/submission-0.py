class Solution:
    def check(self, nums: List[int]) -> bool:
        dec = False
        n = len(nums)

        for i in range(n):
            if nums[(i+1)%n] < nums[i]:
                if dec:
                    return False
                dec = True
        
        return True