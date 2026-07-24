class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        i = 0

        while i < n and nums[i] <= 0:
            left, right = i+1, n-1

            while left < right:
                if nums[i] + nums[left] + nums[right] <= 0:
                    if nums[i] + nums[left] + nums[right] == 0:
                        res.append([nums[i], nums[left], nums[right]])

                    while left < n-1 and nums[left] == nums[left+1]:
                        left += 1
                    
                    left += 1
                
                else:
                    while right > left and nums[right] == nums[right-1]:
                        right -= 1
                    
                    right -= 1

            while i < n-1 and nums[i] == nums[i+1]:
                i += 1
            
            i += 1

        return res