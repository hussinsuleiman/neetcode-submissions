class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        window = defaultdict(int)

        required = len(need)
        have = 0

        best_len = float('inf')
        best_left = 0
        cur_left = 0

        for right, c in enumerate(s):
            window[c] += 1

            if c in need and window[c] == need[c]:
                have += 1
            
            while have == required:
                cur_len = right - cur_left + 1

                if cur_len < best_len:
                    best_len = cur_len
                    best_left = cur_left
                
                window[s[cur_left]] -= 1

                if s[cur_left] in need and window[s[cur_left]] < need[s[cur_left]]:
                    have -= 1
                
                cur_left += 1

        if best_len == float('inf'):
            return ''
        
        return s[best_left : best_left + best_len]