class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []
        n = 0
        i = 1
        j = len(nums)-1

        while n < len(nums):
            while i < j:
                s = nums[n] + nums[i] + nums[j]
                
                if s == 0:
                    output.append([nums[n], nums[i], nums[j]])
                    while i < len(nums)-1 and nums[i] == nums[i+1]:
                        i += 1
                    i += 1
                    while j > 0 and nums[j] == nums[j-1]:
                        j -= 1
                    j -= 1
                elif s > 0:
                    j -= 1
                else:
                    i += 1
            
            while n < len(nums)-1 and nums[n] == nums[n+1]:
                n += 1
            
            n += 1
            i = n + 1
            j = len(nums)-1
        
        return output
        