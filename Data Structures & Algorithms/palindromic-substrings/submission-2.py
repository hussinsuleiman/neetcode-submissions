class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 1
        prev = [0]
        n = len(s)

        for i in range(1, n):
            new = [i]
            count += 1

            if s[i-1] == s[i]:
                new.append(i-1)
                count += 1
            
            for left in prev:
                if left > 0 and s[left-1] == s[i]:
                    new.append(left-1)
                    count += 1
            
            prev = new
        
        return count