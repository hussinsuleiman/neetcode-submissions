class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        
        for c in s:
            if c != ']':
                stack.append(c)
                continue
            
            inner = []

            while stack[-1] != '[':
                inner.append(stack.pop())
            
            stack.pop()
            inner = ''.join(inner[::-1])
            nb = 0
            exp = 0

            while stack and stack[-1].isdigit():
                nb += (ord(stack.pop()) - ord('0')) * 10**exp
                exp += 1

            for i in range(nb):
                stack.append(inner)

        return ''.join(stack)