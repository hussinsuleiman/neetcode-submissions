class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        res = []
        nbOnes = 0

        for elt in s:
            if elt == '1':
                nbOnes += 1
        
        for i in range(nbOnes-1):
            res.append('1')
        
        for i in range(len(s)-nbOnes):
            res.append('0')
        
        res.append('1')
        return ''.join(res)