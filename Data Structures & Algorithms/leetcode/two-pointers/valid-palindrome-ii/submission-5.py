class Solution:
    def validPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s)-1
        deletedR = False
        deletedL = False
        iDelL = 0
        jDelL = j

        while i < j:
            if s[i] != s[j]:
                if deletedR:
                    return False
                
                elif deletedL:
                    i = iDelL
                    j = jDelL
                    deletedR = True
                    continue
            
                elif s[i+1] == s[j]:
                    iDelL = i
                    jDelL = j-1
                    i += 1
                    deletedL = True
                
                elif s[i] == s[j-1]:
                    j -= 1
                    deletedR = True
                else:
                    return False
            
            i += 1
            j -= 1
        
        return True