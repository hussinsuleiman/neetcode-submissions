class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        occ = defaultdict(int)
        nbOdd = 0

        for i in s:
            occ[i] += 1
        
        for i in occ.keys():
            if occ[i]%2 == 1:
                nbOdd += 1

                if nbOdd == 2:
                    return False
        
        return True
