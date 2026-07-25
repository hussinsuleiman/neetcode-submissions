class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l, r = 0, n-1

        while l < r:
            mid = (l+r)//2

            if nums[mid] == target:
                return mid

            if nums[mid] > nums[l]:
                if nums[l] > target or nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            
            elif nums[mid] < nums[l]:
                if nums[r] >= target and nums[mid] <= target:
                    l = mid + 1
                else:
                    r = mid - 1
            
            elif nums[(mid+1)%n] == target:
                return (mid+1)%n
            
            else:
                break

        return l if nums[l] == target else -1