class FreqStack:
    def __init__(self):
        self.time = 0
        self.heap = []
        self.dico = defaultdict(int)

    def push(self, val: int) -> None:
        self.dico[val] += 1
        heapq.heappush(self.heap, (-self.dico[val], -self.time, val))
        self.time += 1

    def pop(self) -> int:
        occ, t, val = heapq.heappop(self.heap)
        self.dico[val] -= 1
        return val

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()