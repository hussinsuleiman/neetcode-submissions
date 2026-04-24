class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        times = dict()
        n = len(position)

        for i in range(n):
            times[position[i]] = (target-position[i]) / float(speed[i])
        
        stack = []
        position.sort()
        stack.append(times[position[-1]])

        for i in range(n-2,-1,-1):
            if times[position[i]] > stack[-1]:
                stack.append(times[position[i]])

        return len(stack)  

