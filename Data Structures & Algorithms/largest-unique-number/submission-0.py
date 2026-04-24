class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        once = set()
        twice = set()

        for elt in nums:
            if elt in once:
                once.remove(elt)
                twice.add(elt)

            elif elt not in twice:
                once.add(elt)
        
        if not once:
            return -1
        
        return max(once)