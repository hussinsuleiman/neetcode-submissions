class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        merged = [(position[i], speed[i]) for i in range(n)]
        merged.sort()
        cur = merged[-1]
        res = 1

        for i in range(n-2, -1, -1):
            if merged[i][1] > cur[1] and (cur[0] - merged[i][0]) / (merged[i][1] - cur[1]) <= (target - cur[0]) / (cur[1]):
                continue

            res += 1
            cur = merged[i]
        
        return res