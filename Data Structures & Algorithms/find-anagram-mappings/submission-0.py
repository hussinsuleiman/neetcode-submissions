class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ind = defaultdict(list)
        out = []

        for i in range(len(nums2)):
            ind[nums2[i]].append(i)
        
        for elt in nums1:
            out.append(ind[elt][-1])
            ind[elt].pop()
        
        return out