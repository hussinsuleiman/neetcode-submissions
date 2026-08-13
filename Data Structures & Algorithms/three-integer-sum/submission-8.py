class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        i = 0
        res = []
        
        while i < n-2:
            j = i+1
            k = n-1

            while j < k:
                if nums[i] + nums[j] + nums[k] == 0:
                    res.append([nums[i], nums[j], nums[k]])

                    while j < n-1 and nums[j+1] == nums[j]:
                        j += 1
                    
                    j += 1

                    while k > j and nums[k] == nums[k-1]:
                        k -= 1
                    
                    k -= 1

                elif nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                
                else:
                    k -= 1

            while i < n-1 and nums[i+1] == nums[i]:
                i += 1
            
            i += 1

        return res  