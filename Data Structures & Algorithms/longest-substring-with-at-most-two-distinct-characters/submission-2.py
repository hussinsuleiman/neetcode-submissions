class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        chars = dict()
        i, j, l = 0, 0, len(s)
        res = 0

        while j < l:
            if s[j] not in chars:
                if len(chars) == 2:
                    res = max(res, j-i)
                    m = min(chars.values())
                    i = m+1

                    for elt in chars:
                        if chars[elt] == m:
                            del chars[elt]
                            break

                chars[s[j]] = j

            chars[s[j]] = j
            j += 1

        return max(res, j-i)