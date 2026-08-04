class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        cur = []
        n = len(nums)

        def backtrack(idx):
            if idx == n:
                res.append(cur.copy())
                return
            
            cur.append(nums[idx])
            backtrack(idx+1)
            cur.remove(nums[idx])
            backtrack(idx+1)
        
        backtrack(0)
        return res