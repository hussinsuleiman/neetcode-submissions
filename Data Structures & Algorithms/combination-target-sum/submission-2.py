class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        cur = []
        n = len(nums)

        def backtrack(ind, rem):
            if rem == 0:
                res.append(cur.copy())
                return
            
            if ind >= n or rem < 0:
                return

            cur.append(nums[ind])
            backtrack(ind, rem-nums[ind])
            cur.pop()
            backtrack(ind + 1, rem)

        backtrack(0, target)
        return res