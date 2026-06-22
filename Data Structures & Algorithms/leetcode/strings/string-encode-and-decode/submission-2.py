class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""

        for s in strs:
            res += str(len(s)) + "#" + s
        
        return res

    def decode(self, s: str) -> List[str]:
        output = []
        i = 0
        j = i
        
        while i < len(s):
            while j < len(s) and s[j] != "#":
                j += 1
            
            n = int(s[i:j])
            j += 1
            i = j
            j += n
            output.append(s[i:j])
            i = j
        
        return output