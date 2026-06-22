class Solution:
    def maxDifference(self, s: str) -> int:
        dico = defaultdict(int)

        for i in range(len(s)):
            dico[s[i]] += 1
        
        oddMax = 0
        evenMin = 100

        for elt in dico.keys():
            if dico[elt] % 2 == 0:
                evenMin = min(evenMin, dico[elt])
            else:
                oddMax = max(oddMax, dico[elt])
        
        return oddMax-evenMin

