class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]

        top = nums[-1]
        prev = self.permuteUnique(nums[:len(nums)-1])
        ans = set()
        res = []

        for p in prev:
            new = p[:]

            for i in range(len(nums)):
                p.insert(i, top)

                if tuple(p) not in ans:
                    ans.add(tuple(p))
                    res.append(p)
                
                p = new[:]
        
        return res