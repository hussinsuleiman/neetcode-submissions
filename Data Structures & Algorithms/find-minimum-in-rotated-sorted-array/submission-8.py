class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n-1

        while l < r:
            mid = (l+r)//2

            if nums[mid] > nums[l]:
                l = mid
            elif l == mid:
                if nums[l] < nums[r]:
                    l += 1
                else:
                    r -= 1
            else:
                r = mid - 1
        
        return nums[(l+1)%n]