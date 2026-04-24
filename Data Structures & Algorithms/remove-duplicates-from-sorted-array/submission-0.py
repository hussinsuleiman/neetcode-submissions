class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        j = 1
        l = len(nums)
        output = 1

        while j < l:
            if nums[j] == nums[i]:
                j += 1
            else:
                i += 1
                if i < j:
                    nums[i] = nums[j]
                j += 1
                output += 1
        
        return output