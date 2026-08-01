from collections import deque

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = {char: set() for word in words for char in word}
        indegree = {char: 0 for char in graph}

        for i in range(len(words) - 1):
            first, second = words[i], words[i + 1]
            l1, l2 = len(first), len(second)
            limit = min(l1, l2)

            if l1 > l2 and first[:l2] == second:
                return ""

            for j in range(limit):
                if first[j] != second[j]:
                    if second[j] not in graph[first[j]]:
                        graph[first[j]].add(second[j])
                        indegree[second[j]] += 1
                    break

        queue = deque(char for char in indegree if indegree[char] == 0)
        order = []

        while queue:
            char = queue.popleft()
            order.append(char)

            for neighbor in graph[char]:
                indegree[neighbor] -= 1

                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        if len(order) < len(graph):
            return ""

        return ''.join(order)