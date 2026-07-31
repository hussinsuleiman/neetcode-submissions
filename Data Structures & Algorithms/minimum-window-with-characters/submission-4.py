class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dicT = dict()
        need = 0

        for c in t:
            if c in dicT:
                dicT[c] += 1
            else:
                need += 1
                dicT[c] = 1

        l,r = 0,0
        lS = len(s)
        have = 0
        cur = defaultdict(int)
        res = ''
        best = lS

        while r <= lS:
            while have == need:
                cur[s[l]] -= 1
                
                if s[l] in dicT and dicT[s[l]] > cur[s[l]]:
                    have -= 1
                    
                    if r-l <= best:
                        best = r-l
                        res = s[l:r]

                l += 1
            
            if r == lS:
                break

            cur[s[r]] += 1

            if s[r] in dicT and dicT[s[r]] == cur[s[r]]:
                have += 1

            r += 1
            
        return res