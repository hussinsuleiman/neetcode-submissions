class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dico = dict()
        res = [-1] * len(nums1)

        for i,n in enumerate(nums2):
            dico[n] = i
        
        for i,n in enumerate(nums1):
            for k in range(dico[n]+1, len(nums2)):
                if nums2[k] > n:
                    res[i] = nums2[k]
                    break
        
        return res