class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = [0] * (len(nums)+1)

        for i in range(1, len(nums)+1):
            prefix[i] = prefix[i-1] + nums[i-1]
        
        dico = defaultdict(int)
        dico[0] = 1
        res = 0

        for j in range(1, len(nums)+1):
            res += dico[prefix[j]-k]
            dico[prefix[j]] += 1
        
        return res