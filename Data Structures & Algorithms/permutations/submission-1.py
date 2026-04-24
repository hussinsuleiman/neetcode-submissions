class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]

        prev = self.permute(nums[1:])
        res = []

        for p in prev:
            new = p + [nums[0]]
            res.append(new.copy())

            for i in range(len(nums)-1):
                temp = new[i]
                new[i] = new[i-1]
                new[i-1] = temp
                res.append(new.copy())
        
        return res

