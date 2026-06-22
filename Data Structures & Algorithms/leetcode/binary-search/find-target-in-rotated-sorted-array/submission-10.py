class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums)-1

        while i < j:
            mid = (i+j) // 2

            if nums[mid] == target:
                return mid

            elif i == mid:
                i += 1
                break

            elif nums[mid] > target:
                if nums[j] > target:
                    if nums[mid] > nums[j]:
                        i = mid
                    else:
                        j = mid
                else:
                    j = mid

            elif nums[i] > target:
                i = mid

            elif nums[mid] > nums[i]:
                i = mid
            
            else:
                j = mid
        
        if nums[i] == target:
            return i
        return -1
