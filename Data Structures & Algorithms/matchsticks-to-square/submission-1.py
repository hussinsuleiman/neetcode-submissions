class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        s = sum(matchsticks)

        if s%4 != 0 or max(matchsticks) > s//4:
            return False
        
        n = len(matchsticks)
        lengths = [0,0,0,0]
        matchsticks.sort()

        def backtrack(i):
            if i < 0:
                for l in lengths:
                    if l != s//4:
                        return False

                return True
            
            for x in range(4):
                if lengths[x] + matchsticks[i] <= s//4:
                    lengths[x] += matchsticks[i]
                    ans = backtrack(i-1)
                    
                    if ans:
                        return True

                    lengths[x] -= matchsticks[i]
            
            return False
        
        return backtrack(n-1)