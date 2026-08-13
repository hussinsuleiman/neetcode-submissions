class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = []
        l = 0

        while columnNumber > 0:
            if columnNumber%26 == 0:
                res.append(26)
                columnNumber -= 1
            else:
                res.append(columnNumber%26)
            
            columnNumber //= 26
            l += 1

        ans = []

        for i in range(l-1, -1, -1):
            ans.append(chr(res[i] + ord('A') - 1))

        return ''.join(ans) 