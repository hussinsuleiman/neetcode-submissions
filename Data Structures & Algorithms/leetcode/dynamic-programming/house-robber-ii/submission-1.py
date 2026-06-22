class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]
        elif n == 2:
            return max(nums[0], nums[1])
        
        dp1 = [nums[0], max(nums[0], nums[1])]
        dp2 = [nums[1], max(nums[1], nums[2])]

        for i in range(2, n-1):
            dp1.append(max(dp1[i-1], dp1[i-2] + nums[i]))
            dp2.append(max(dp2[i-1], dp2[i-2] + nums[i+1]))

        return max(dp1[n-2], dp2[n-2])