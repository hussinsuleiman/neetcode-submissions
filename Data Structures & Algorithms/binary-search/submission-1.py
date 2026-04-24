class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums)

        while i < j:
            m = (i+j) // 2

            if nums[m] == target:
                return m
            elif nums[m] < target:
                i = m
                if m == i:
                    i += 1
            else:
                j = m
        
        return -1