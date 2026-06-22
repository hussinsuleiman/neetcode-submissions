class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        l = len(nums)
        nums.sort()

        def dfs(i, currSet):
            if i == l:
                return [currSet]

            res = dfs(i+1, currSet + [nums[i]]) 
            while i < l-1 and nums[i] == nums[i+1]:
                i += 1
            return res + dfs(i+1, currSet)
        
        return dfs(0, [])