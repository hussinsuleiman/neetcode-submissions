class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        n = len(nums)

        def canSplit(max_sum):
            pieces = 1
            cur = 0

            for i in range(n):
                if cur + nums[i] <= max_sum:
                    cur += nums[i]
                else:
                    pieces += 1
                    cur = nums[i]
            
            return pieces <= k

        right = sum(nums)
        left = max(nums)

        while left < right:
            mid = (left + right) // 2

            if canSplit(mid):
                right = mid
            else:
                left = mid+1
        
        return left