class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        seen = dict()
        seen[0] = -1
        cur = 0
        l = len(nums)

        for i in range(l):
            cur = (cur + nums[i]) % k

            if cur in seen:
                if seen[cur] != i-1:
                    return True
            else:
                seen[cur] = i

        return False
