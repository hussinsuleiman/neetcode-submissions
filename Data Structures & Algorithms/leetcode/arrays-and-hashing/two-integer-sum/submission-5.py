class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dico = dict()

        for i in range(len(nums)):
            if target-nums[i] in dico.keys():
                return [dico[target-nums[i]], i]
            else:
                dico[nums[i]] = i