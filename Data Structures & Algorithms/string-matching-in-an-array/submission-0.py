class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = []

        for i in range(len(words)):
            valid = False

            for j in range(len(words)):   
                if i == j:
                    continue

                for k in range(len(words[j]) - len(words[i]) + 1):
                    nxt = words[j][k:k+len(words[i])]

                    if nxt == words[i]:
                        res.append(words[i])
                        valid = True
                        break
                
                if valid:
                    break
        
        return res