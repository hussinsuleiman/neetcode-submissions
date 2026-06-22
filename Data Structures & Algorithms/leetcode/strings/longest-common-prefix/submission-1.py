class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        m = 200

        for i in range(len(strs)):
            m = min(m, len(strs[i]))

        p = []
        done = False

        for i in range(m):
            for j in range(1, len(strs)):
                if strs[j][i] != strs[0][i]:
                    done = True
            
            if done:
                break
            p.append(strs[0][i])
        
        return "".join(p)