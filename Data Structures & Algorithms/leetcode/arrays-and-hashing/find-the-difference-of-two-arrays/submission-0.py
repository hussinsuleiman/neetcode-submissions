class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        s1, s2 = set(nums1), set(nums2)
        ans = [[], []]

        for elt in s1:
            if elt not in s2:
                ans[0].append(elt)
        
        for elt in s2:
            if elt not in s1:
                ans[1].append(elt)
        
        return ans