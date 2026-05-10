class FreqStack:
    def __init__(self):
        self.freq = defaultdict(int)
        self.gps = defaultdict(list)
        self.maxf = 0

    def push(self, val: int) -> None:
        self.freq[val] += 1
        f = self.freq[val]
        self.gps[f].append(val)

        if f > self.maxf:
            self.maxf = f

    def pop(self) -> int:
        val = self.gps[self.maxf].pop()
        self.freq[val] -= 1

        if not self.gps[self.maxf]:
            self.maxf -= 1

        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()