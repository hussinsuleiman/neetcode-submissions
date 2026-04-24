class Solution:
    def encode(self, strs: List[str]) -> str: 
        res = ""

        for i in range(len(strs)):
            res += str(len(strs[i])) + "#" + strs[i]

        return res        

    def decode(self, s: str) -> List[str]:
        output = []
        i = 0

        while i < len(s):
            j = i
            
            while s[j] != "#":
                j += 1
            
            n = int(s[i:j])
            i = j + 1
            j = i + n
            output.append(s[i:j])
            i = j

        return output


