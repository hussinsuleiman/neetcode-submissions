class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        def expand(l: int, r: int):
            while l > -1 and r < n and s[l] == s[r]:
                l -= 1
                r += 1

            return (l,r)

        res_idx = 0
        res_len = 0

        for i in range(n):
            odd_l, odd_r = expand(i, i)
            if odd_r - odd_l - 1 > res_len:
                res_len = odd_r - odd_l - 1
                res_idx = odd_l+1

            even_l, even_r = expand(i, i+1)
            if even_r - even_l - 1 > res_len:
                res_len = even_r - even_l - 1
                res_idx = even_l+1

        return s[res_idx: res_idx + res_len]