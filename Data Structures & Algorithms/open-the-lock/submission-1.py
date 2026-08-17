class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        graph = defaultdict(list)
        seen = set(deadends)

        if '0000' in seen:
            return -1

        for i in range(10):
            for j in range(10):
                for k in range(10):
                    for l in range(10):
                        s = str(i) + str(j) + str(k) + str(l)

                        if s in seen:
                            continue

                        graph[s].append(str((i+1)%10) + str(j) + str(k) + str(l))
                        graph[s].append(str((i-1)%10) + str(j) + str(k) + str(l))
                        graph[s].append(str(i) + str((j+1)%10) + str(k) + str(l))
                        graph[s].append(str(i) + str((j-1)%10) + str(k) + str(l))
                        graph[s].append(str(i) + str(j) + str((k+1)%10) + str(l))
                        graph[s].append(str(i) + str(j) + str((k-1)%10) + str(l))
                        graph[s].append(str(i) + str(j) + str(k) + str((l+1)%10))
                        graph[s].append(str(i) + str(j) + str(k) + str((l-1)%10))

        queue = deque(['0000'])
        seen.add('0000')
        dist = 0

        while queue and target not in seen:
            l = len(queue)

            for i in range(l):
                top = queue.popleft()

                for nei in graph[top]:
                    if nei not in seen:
                        queue.append(nei)
                        seen.add(nei)

            dist += 1
        
        return dist if target in seen else -1