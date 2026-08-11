class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cur = 0
        n = len(nums)
        
        while cur < n and nums[cur] == 0:
            cur += 1

        for i in range(cur+1,n):
            if nums[i] == 0:
                nums[i], nums[cur] = nums[cur], nums[i]
                cur += 1

        cur = n-1

        while cur >= 0 and nums[cur] == 2:
            cur -= 1

        for i in range(cur-1, -1, -1):
            if nums[i] == 2:
                nums[i], nums[cur] = nums[cur], nums[i]
                cur -= 1