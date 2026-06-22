class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cur = 0
        count = 0

        for i in range(len(nums)):
            if cur == nums[i]:
                count += 1
            elif count == 0:
                cur = nums[i]
                count = 1
            else:
                count -= 1
        
        return cur