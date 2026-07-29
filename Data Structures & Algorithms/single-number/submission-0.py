class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = defaultdict(int)

        for n in nums:
            d[n] += 1
        
        for n in nums:
            if d[n] == 1:
                return n