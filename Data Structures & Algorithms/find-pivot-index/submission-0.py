class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        pre = [0] * n

        for i in range(1, n):
            pre[i] = pre[i-1] + nums[i-1]
        
        s = pre[-1] + nums[-1]

        for i in range(n):
            if 2*pre[i] + nums[i] == s:
                return i

        return -1 
