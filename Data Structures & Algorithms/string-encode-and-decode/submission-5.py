class Solution:
    def encode(self, strs: List[str]) -> str:
        arr = []

        for s in strs:
            arr.append(str(len(s)) + '#' + s)
        
        return ''.join(arr)

    def decode(self, s: str) -> List[str]:
        res = []
        l = len(s)
        elt = []
        i = 0

        while i < l: 
            nb = 0

            while i < l and ord('0') <= ord(s[i]) and ord(s[i]) <= ord('9'):
                nb = nb*10 + ord(s[i])-ord('0')
                i += 1
            
            i += 1

            for k in range(nb):
                elt.append(s[i])
                i += 1

            res.append(''.join(elt))
            elt = []
        
        return res