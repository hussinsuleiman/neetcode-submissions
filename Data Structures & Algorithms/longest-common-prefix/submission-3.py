class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pre = []
        m = len(strs[0])

        for s in strs:
            m = min(m, len(s))

        i = 0

        while i < m:
            for s in strs:
                if s[i] != strs[0][i]:
                    return ''.join(pre)
            
            pre.append(s[i])
            i += 1

        return ''.join(pre)