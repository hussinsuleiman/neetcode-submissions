class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nbs = set(nums)
        starts = set()

        for nb in nbs:
            if nb-1 not in nbs:
                starts.add(nb)
        
        output = 0

        for nb in starts:
            length = 1
            while nb+1 in nums:
                length += 1
                nb += 1
            output = max(length, output)

        return output