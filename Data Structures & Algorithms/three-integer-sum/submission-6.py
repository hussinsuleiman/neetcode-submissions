class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        i = 0

        while i < n:
            elts = set()
            j = i+1

            while j < n:
                if -nums[j] in elts:
                    res.append([nums[i], nums[j], -nums[i]-nums[j]])
                    
                    while j < n-1 and nums[j] == nums[j+1]:
                        j += 1
                else:
                    elts.add(nums[i] + nums[j])
                
                j += 1

            while i < n-1 and nums[i] == nums[i+1]:
                i += 1
            
            i += 1

        return res