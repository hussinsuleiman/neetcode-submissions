class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        res = []
        i = 0

        for n in nums:
            while queue and i-queue[0][1] >= k:
                queue.popleft()

            while queue and queue[-1][0] <= n:
                queue.pop()

            queue.append((n,i))
            i += 1

            if i >= k:
                res.append(queue[0][0])
        
        return res