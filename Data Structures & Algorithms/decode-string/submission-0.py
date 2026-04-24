class Solution:
    def decodeString(self, s: str) -> str:
        stack, i = [], 0
        l = len(s)

        while i < l:
            while i < l and s[i] != ']':
                stack.append(s[i])
                i += 1
            
            cur = []

            while stack and stack[-1] != '[':
                cur.append(stack.pop())
            
            nb = ''

            if stack:
                stack.pop()

                while stack and '0' <= stack[-1] <= '9':
                    nb = stack.pop() + nb
            else:
                nb = 1

            cur.reverse()

            if nb:
                stack.append(int(nb) * ''.join(cur))

            i += 1

        return ''.join(stack)        