class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        l = len(s)
        left = deque()
        left.append(0)
        check = 0

        while left:
            top = left.popleft()

            if top == l-1:
                return True

            for i in range(max(check, top+minJump), top+maxJump+1):
                if i < l and s[i] == '0':
                    left.append(i)
            
            check = top+maxJump+1

        return False 