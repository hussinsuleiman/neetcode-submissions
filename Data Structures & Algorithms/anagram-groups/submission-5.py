class Solution:
    def anagram(self, a, b):
        cnt = [0] * 26

        for c in a:
            cnt[ord(c) - ord('a')] += 1
        
        for c in b:
            cnt[ord(c) - ord('a')] -= 1
        
        for i in range(26):
            if cnt[i] != 0:
                return False
        
        return True

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dico = defaultdict(list)
        res = []

        for s in strs:
            done = False

            for key in dico:
                if self.anagram(s, key):
                    dico[key].append(s)
                    done = True
                    break
            
            if not done:
                dico[s] = [s]
        
        for key in dico:
            res.append(dico[key])
        
        return res