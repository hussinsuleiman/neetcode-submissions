class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        nbs = [0, 0, 0]
        l = len(nums)

        for n in nums:
            nbs[n] += 1
        
        for i in range(nbs[0]):
            nums[i] = 0
        
        for i in range(nbs[0], nbs[0] + nbs[1]):
            nums[i] = 1
        
        for i in range(nbs[0] + nbs[1], l):
            nums[i] = 2
        
        