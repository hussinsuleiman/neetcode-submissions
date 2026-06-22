class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(i, currSum, currSet):
            if currSum == target:
                res.append(currSet.copy())
                return

            if i >= len(candidates) or currSum > target:
                return
            
            currSet.append(candidates[i])
            dfs(i+1, currSum + candidates[i], currSet)
            currSet.pop()

            while i < len(candidates)-1 and candidates[i] == candidates[i+1]:
                i += 1    
            dfs(i+1, currSum, currSet)
        
        dfs(0, 0, [])
        return res