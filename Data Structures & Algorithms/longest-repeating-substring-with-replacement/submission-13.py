class Solution:
    def characterReplacement(self, s: str, k: int) -> int:       
        i = 0
        j = 0
        lenMax = 1
        maxf = 1
        occChar = defaultdict(int)

        while j < len(s):
            occChar[s[j]] += 1
            
            if occChar[s[j]] >= maxf:
                maxf = occChar[s[j]]
            
            while (j-i+1-maxf) > k:
                occChar[s[i]] -= 1
                i += 1
            
            lenMax = max(lenMax, j-i+1)
            j += 1

        return lenMax


            
            

        