class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nbToInd = dict()

        for i in range(len(nums)):
            if target-nums[i] in nbToInd:
                return [nbToInd[target-nums[i]], i]
            else:
                nbToInd[nums[i]] = i