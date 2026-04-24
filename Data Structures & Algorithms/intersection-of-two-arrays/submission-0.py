class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s = set(nums1)
        t = set(nums2)
        out = []

        for elt in s:
            if elt in t:
                out.append(elt)
        
        return out
        