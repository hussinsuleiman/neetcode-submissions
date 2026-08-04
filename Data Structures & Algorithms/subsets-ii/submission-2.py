class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        cur = []

        def backtrack(idx):
            if idx == n:
                res.append(cur.copy())
                return

            cur.append(nums[idx])
            backtrack(idx+1)
            cur.pop()
            i = idx+1

            while i < n and nums[i] == nums[idx]:
                i += 1
            
            backtrack(i)
        
        backtrack(0)
        return res