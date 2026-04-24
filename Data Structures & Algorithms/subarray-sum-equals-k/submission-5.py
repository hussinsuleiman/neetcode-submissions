class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSums = defaultdict(int)
        prefixSums[0] = 1
        currPrefix = 0
        output = 0

        for num in nums:
            currPrefix += num
            if currPrefix - k in prefixSums.keys():
                output += prefixSums[currPrefix-k]
            prefixSums[currPrefix] += 1
        
        return output