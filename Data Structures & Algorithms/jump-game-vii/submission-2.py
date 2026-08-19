class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if s[-1] == '1':
            return False
        
        n = len(s)
        queue = deque([0])
        farthest = 0
        seen = set([0])

        while queue:
            top = queue.popleft()

            for i in range(max(farthest+1, top+minJump), min(top + maxJump + 1, n)):
                if s[i] == '0':
                    queue.append(i)
                    seen.add(i)

            farthest = top + maxJump
        
        return n-1 in seen