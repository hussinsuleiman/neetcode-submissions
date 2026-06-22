class Solution:
    def validPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s)-1
        deletedR = False
        deletedL = False
        iDelL = 0
        jDelL = j
        iDelR = 0
        jDelR = j

        while i < j:
            if s[i] != s[j]:
                if deletedR or deletedL:
                    if deletedR and deletedL:
                        return False
                    elif deletedL:
                        i = iDelL
                        j = jDelL
                        deletedR = True
                        continue
                    else:
                        i = iDelR
                        j = jDelR
                        deletedL = True
                        continue

                elif s[i+1] == s[j]:
                    iDelL = i
                    jDelL = j-1
                    i += 1
                    deletedL = True
                elif s[i] == s[j-1]:
                    iDelR = i+1
                    jDelR = j
                    j -= 1
                    deletedR = True
                else:
                    return False
            
            i += 1
            j -= 1
        
        return True