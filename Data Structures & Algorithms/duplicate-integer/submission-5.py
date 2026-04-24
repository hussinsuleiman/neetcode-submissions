class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        elts = set()
        for i in range(len(nums)):
            if nums[i] in elts:
                return True
            elts.add(nums[i])
        return False
        