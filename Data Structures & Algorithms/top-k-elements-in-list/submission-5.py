class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        buckets = [[] for i in range(n+1)]
        dico = defaultdict(int)

        for i in range(n):
            dico[nums[i]] += 1
        
        for key in dico:
            buckets[dico[key]].append(key)
        
        res = []
        l = 0

        for i in range(n, -1, -1):
            if l >= k:
                break
                
            res += buckets[i]
            l += len(buckets[i])

        return res