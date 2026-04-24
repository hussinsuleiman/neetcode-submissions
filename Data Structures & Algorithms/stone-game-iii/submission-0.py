class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        dp = [(0,0)]
        n = len(stoneValue)

        for i in range(1, n+1):
            a,b = -1000000000, 1000000000
            c = stoneValue[-i]

            for j in range(1, min(i, 3)+1):
                a = max(a, c + dp[-j][1])
                b = min(b, -c + dp[-j][0])
                c += stoneValue[-i+j]

            dp.append((a,b))

        if dp[-1][0] == 0:
            return "Tie"
        
        if dp[-1][0] > 0:
            return "Alice"
        
        return "Bob"