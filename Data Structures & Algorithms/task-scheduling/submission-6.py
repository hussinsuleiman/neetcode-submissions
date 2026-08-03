class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time = 0
        cnt = defaultdict(int)
        active = []
        idle = deque()
        nb = len(tasks)

        for task in tasks:
            cnt[task] += 1
        
        for task in cnt:
            heapq.heappush(active, (-cnt[task], task))
        
        while nb > 0:
            if active:
                c,task = heapq.heappop(active)
                nb -= 1
                cnt[task] -= 1

                if cnt[task] > 0:
                    idle.append((time + n, task))

            while idle:
                t, task = idle[0]

                if t == time:
                    idle.popleft()
                    heapq.heappush(active, (-cnt[task], task))
                else:
                    break

            time += 1

        return time