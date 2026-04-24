class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for i in range(len(nums))]
        count = defaultdict(int)

        for n in nums:
            count[n] += 1
        
        for t in count.keys():
            freq[count[t]-1].append(t)
        
        nbChosen = 0
        index = len(nums)-1
        output = []

        while nbChosen < k:
            for nb in freq[index]:
                output.append(nb)
                nbChosen += 1
            index -= 1

        return output