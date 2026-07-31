class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        cnt = defaultdict(int)
        n1 = len(s1)
        n2 = len(s2)

        if n1 > n2:
            return False

        for c in s1:
            cnt[c] += 1
        
        cur = defaultdict(int)

        for c in range(n1):
            cur[s2[c]] += 1
        
        right = n1

        while right <= n2:
            done = True

            for c in cnt:
                if cur[c] != cnt[c]:
                    if right == n2:
                        return False
                        
                    cur[s2[right]] += 1
                    cur[s2[right-n1]] -= 1
                    done = False
                    break
            
            if done:
                return True
        
            right += 1

        return False