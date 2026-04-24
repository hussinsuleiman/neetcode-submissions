class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums
        
        a = self.sortArray(nums[:len(nums) // 2])
        b = self.sortArray(nums[len(nums) // 2:])

        i = 0
        j = 0
        output = []

        while i < len(a) and j < len(b):
            if a[i] < b[j]:
                output.append(a[i])
                i += 1
            else:
                output.append(b[j])
                j += 1
        
        if i == len(a):
            for k in range(j, len(b)):
                output.append(b[k])
        else:
            for k in range(i, len(a)):
                output.append(a[k])

        return output
