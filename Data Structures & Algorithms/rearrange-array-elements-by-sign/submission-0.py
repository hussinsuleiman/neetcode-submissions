class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        new = []
        l = len(nums)
        pos, neg = [], []

        for i in range(l):
            if nums[i] > 0:
                pos.append(nums[i])
            else:
                neg.append(nums[i])
        
        for i in range(l//2):
            new.append(pos[i])
            new.append(neg[i])
        
        return new