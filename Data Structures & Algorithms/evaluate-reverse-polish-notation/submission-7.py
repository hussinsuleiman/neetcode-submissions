class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for c in tokens:
            if c == '+':
                stack.append(stack.pop() + stack.pop())
            
            elif c == '-':
                a,b = stack.pop(), stack.pop()
                stack.append(b-a)

            elif c == '*':
                stack.append(stack.pop() * stack.pop())
            
            elif c == '/':
                a,b = stack.pop(), stack.pop()
                
                if a*b >= 0 or b%a == 0:
                    stack.append(b//a)
                else:
                    stack.append(b//a+1)

            else:
                stack.append(int(c))

        return stack[0] 