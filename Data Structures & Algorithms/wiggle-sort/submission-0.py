class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        i,j = 0, len(nums)-1
        ans = []

        while i < j:
            ans.append(nums[i])
            ans.append(nums[j])
            i += 1
            j -= 1
        
        if i == j:
            ans.append(nums[i])
        
        for i in range(len(nums)):
            nums[i] = ans[i]