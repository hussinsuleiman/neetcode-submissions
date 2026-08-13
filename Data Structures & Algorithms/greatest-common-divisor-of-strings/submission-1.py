class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        l1,l2 = len(str1), len(str2)

        for i in range(min(l1, l2), 0, -1):
            if l1%i == 0 and l2%i == 0:
                valid = True
                s1 = str1[:i]

                for j in range(l1//i):
                    if str1[j*i:j*i+i] != s1:
                        valid = False
                
                if valid:
                    for j in range(l2//i):
                        if str2[j*i:j*i+i] != s1:
                            valid = False
                
                if valid:
                    return s1
        
        return ''