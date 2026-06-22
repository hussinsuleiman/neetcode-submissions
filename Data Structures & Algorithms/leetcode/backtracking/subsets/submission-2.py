class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
       
        def backtrack(curr, index):
            if index == n:
                return [curr]

            subsets = backtrack(curr + [nums[index]], index + 1)
            subsets += backtrack(curr, index + 1)
            return subsets

        return backtrack([], 0)