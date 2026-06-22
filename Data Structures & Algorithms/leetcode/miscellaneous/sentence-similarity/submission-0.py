class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        n = len(sentence1)
        sim = set()

        if len(sentence2) != n:
            return False
        
        for a,b in similarPairs:
            sim.add((a,b))
            sim.add((b,a))

        for i in range(n):
            if (sentence1[i], sentence2[i]) not in sim and sentence1[i] != sentence2[i]:
                return False
        
        return True