class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        i = 0
        l1 = len(s1)
        l2 = len(s2)
        
        def countChar(s, i, j):
            occChar = defaultdict(int)

            for l in range(i, j):
                occChar[s[l]] += 1
            
            return occChar

        occ1 = countChar(s1, 0, l1)

        def checkPerm(k):
            occ = countChar(s2, k, k + l1)

            for l in occ1.keys():
                if occ[l] != occ1[l]:
                    return False
            
            return True
        
        while i <= l2-l1:
            if checkPerm(i):
                return True
            i += 1
        
        return False
        
        
