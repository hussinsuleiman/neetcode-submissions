class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []

        for c in s:
            if len(stack) >= k-1:
                delete = True

                for i in range(1, k):
                    if stack[-i] != c:
                        delete = False
                        break
                
                if delete:
                    for i in range(k-1):
                        stack.pop()
                else:
                    stack.append(c)

            else:
                stack.append(c)
        
        return "".join(stack)