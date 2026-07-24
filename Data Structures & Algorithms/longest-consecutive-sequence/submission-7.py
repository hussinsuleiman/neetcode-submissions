class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        elts = set(nums)
        starts = set()

        for n in nums:
            if n-1 not in elts:
                starts.add(n)
        
        res = 0

        for start in starts:
            cur = 1
            nb = start

            while nb+1 in elts:
                cur += 1
                nb += 1

            res = max(res, cur) 
        
        return res