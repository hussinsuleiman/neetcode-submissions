class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        chars = dict()
        i, j, l = 0, 0, len(s)
        res = 0

        if k == 0:
            return 0

        while j < l:
            if s[j] not in chars and len(chars) >= k:
                res = max(res, j-i)
                m = min(chars.values())
                i = m+1

                for elt in chars:
                    if chars[elt] == m:
                        del chars[elt]
                        break

            chars[s[j]] = j
            j += 1
        
        return max(res, j-i)