class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        s = sum(nums)
        l,r = 0, s-nums[0]
        i = 0

        while i < len(nums):
            if l == r:
                return i

            if i == len(nums)-1:
                break

            l += nums[i]
            r -= nums[i+1]
            i += 1

        return -1