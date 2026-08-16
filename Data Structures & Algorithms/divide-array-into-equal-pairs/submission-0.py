class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        dico = defaultdict(int)

        for n in nums:
            dico[n] += 1
        
        for n in dico:
            if dico[n]%2 == 1:
                return False
        
        return True