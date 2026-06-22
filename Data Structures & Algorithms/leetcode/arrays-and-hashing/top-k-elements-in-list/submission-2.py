class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for i in range(len(nums)+1)] 
        dico = dict()

        for n in nums:
            if n in dico.keys():
                dico[n] += 1
            else:
                dico[n] = 1
        
        for key in dico.keys():
            freq[dico[key]].append(key)
        
        nbChosen = 0
        index = len(nums)
        output = []

        while nbChosen < k:
            for nb in freq[index]:
                output.append(nb)
                nbChosen += 1
            
            index -= 1
        
        return output