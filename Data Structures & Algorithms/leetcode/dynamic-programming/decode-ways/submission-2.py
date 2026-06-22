class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [1, 1 if s[0] != '0' else 0]
        l = len(s)

        for i in range(1, l):
            res = dp[i] if s[i] != '0' else 0

            if s[i-1] == '1' or (s[i-1] == '2' and ord('0') <= ord(s[i]) and ord('6') >= ord(s[i])):
                res += dp[i-1]
            
            dp.append(res)

        return dp[l]
