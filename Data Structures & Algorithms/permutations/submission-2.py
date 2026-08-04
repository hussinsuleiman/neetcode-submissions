class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        
        n = len(nums)
        top = nums.pop()
        prev = self.permute(nums)
        res = []

        for p in prev:
            for i in range(n):
                new = p.copy()
                new.insert(i, top)
                res.append(new)
        
        return res