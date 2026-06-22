class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def genNew(o, c, s):
            output = []
            if o == c:
                if o < n:
                    output = genNew(o+1, c, s + "(")
                else:
                    output.append(s)
            else: 
                output = genNew(o, c+1, s + ")")
                if o < n:
                    output += genNew(o+1, c, s + "(") 
            return output

        return genNew(0, 0, "")