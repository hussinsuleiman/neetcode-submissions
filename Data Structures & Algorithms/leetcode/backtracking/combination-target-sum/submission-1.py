class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, currSum, currSet):
            if currSum == target:
                res.append(currSet.copy())
                return
            if i >= len(nums) or currSum > target:
                return
            
            currSet.append(nums[i])
            dfs(i, currSum + nums[i], currSet)
            currSet.pop()
            dfs(i+1, currSum, currSet)
        
        dfs(0, 0, [])
        return res