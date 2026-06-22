class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        currSum = 0

        for op in operations:
            if op == '+':
                currSum += stack[-1] + stack[-2]
                stack.append(stack[-1] + stack[-2])
            elif op == 'C':
                currSum -= stack[-1]
                stack.pop()
            elif op == 'D':
                currSum += 2 * stack[-1]
                stack.append(2 * stack[-1])
            else:
                currSum += int(op)
                stack.append(int(op))
        
        return currSum