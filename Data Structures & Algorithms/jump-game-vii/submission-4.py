class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        queue = deque([0])
        farthest = 0

        while queue:
            top = queue.popleft()

            for i in range(max(farthest+1, top+minJump), min(top + maxJump + 1, n)):
                if s[i] == '0':
                    queue.append(i)

                    if i == n-1:
                        return True

            farthest = top + maxJump
        
        return False