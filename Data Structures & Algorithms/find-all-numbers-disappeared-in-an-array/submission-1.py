class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        s = set(nums)
        n = len(nums)

        for i in range(1, n+1):
            if i not in s:
                res.append(i)
        
        return res