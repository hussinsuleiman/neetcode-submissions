class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = dict()

        for elt in nums2:
            d[elt] = -1
        
        stack = []

        for i in range(len(nums2)):
            while stack and stack[-1] < nums2[i]:
                a = stack.pop()
                d[a] = nums2[i]

            stack.append(nums2[i])
        
        output = []
        
        for nb in nums1:
            output.append(d[nb])

        return output  