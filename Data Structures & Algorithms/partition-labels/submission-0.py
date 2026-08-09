class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        occ = defaultdict(int)
        n = len(s)

        for c in s:
            occ[c] += 1
        
        l,r = 0,1
        seen = set([s[0]])
        occ[s[0]] -= 1
        res = []

        while r <= n:
            valid = True

            for elt in seen:
                if occ[elt]:
                    valid = False
                    break

            if valid:
                res.append(r-l)
                l = r
                
                if r == n:
                    break
                
                r = l+1
                seen = set([s[l]])
                occ[s[l]] -= 1
            
            else:
                seen.add(s[r])
                occ[s[r]] -= 1
                r += 1
        
        return res