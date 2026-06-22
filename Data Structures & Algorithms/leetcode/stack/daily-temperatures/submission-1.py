class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            if len(stack) == 0:
                stack.append((temperatures[i], i))
            else:
                while len(stack) > 0 and temperatures[i] > stack[-1][0]:
                    temp, index = stack.pop()
                    output[index] = i-index
                stack.append((temperatures[i], i))
        
        return output
