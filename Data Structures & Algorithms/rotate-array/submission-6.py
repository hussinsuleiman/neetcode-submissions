class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k%n

        if k == 0:
            return
        
        i = 0

        while i < (n-k)//2:
            nums[i], nums[n-k-1-i] = nums[n-k-1-i], nums[i]
            i += 1
        
        i = n-k

        while i < (n-k) + k // 2:
            nums[i], nums[2*n-1-i-k] = nums[2*n-1-i-k], nums[i]
            i += 1
        
        i = 0
        
        while i < n // 2:
            nums[i], nums[n-1-i] = nums[n-1-i], nums[i]
            i += 1