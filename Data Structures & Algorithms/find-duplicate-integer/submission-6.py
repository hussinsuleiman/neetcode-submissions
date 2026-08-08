class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast, slow = nums[nums[0]], nums[0]

        while fast != slow:
            fast = nums[nums[fast]]
            slow = nums[slow]
        
        new = 0

        while new != slow:
            slow = nums[slow]
            new = nums[new]
        
        return new