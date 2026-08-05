class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num = nums[0]
        occ = 1
        n = len(nums)

        for i in range(1,n):
            if nums[i] == num:
                occ += 1
            else:
                occ -= 1

                if occ < 0:
                    num = nums[i]
                    occ = 1
            
        return num