class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        heap = nums.copy()
        heapq.heapify(heap)
        dico = defaultdict(list)

        for i in range(len(nums)):
            dico[nums[i]].append(i)

        for i in range(k):
            m = heapq.heappop(heap)

            ind = dico[m][0]
            dico[m] = dico[m][1:]

            m *= multiplier
            dico[m].append(ind)

            dico[m].sort()
            heapq.heappush(heap, m)

        res = [0] * len(nums)

        while heap:
            m = heapq.heappop(heap)
            
            for i in dico[m]:
                res[i] = m
        
        return res