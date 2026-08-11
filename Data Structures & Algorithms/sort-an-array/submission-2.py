class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)

        if n == 0:
            return []
        
        if n == 1:
            return nums
        
        left = self.sortArray(nums[:n//2])
        right = self.sortArray(nums[n//2:])
        res = []
        i,j = 0,0

        while i < n//2 and j < (n+1)//2:
            if left[i] < right[j]:
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                j += 1
        
        while i < n//2:
            res.append(left[i])
            i += 1
        
        while j < (n+1)//2:
            res.append(right[j])
            j += 1
        
        return res