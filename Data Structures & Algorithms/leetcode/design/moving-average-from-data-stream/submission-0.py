class MovingAverage:
    def __init__(self, size: int):
        self.elts = [0] * size
        self.i = 0
        self.s = 0
        self.size = size
        self.cur = 0

    def next(self, val: int) -> float:
        self.s += val - self.elts[self.i]
        self.elts[self.i] = val
        self.i = (self.i+1) % (self.size)
        
        if self.cur < self.size:
            self.cur += 1
        
        return float(self.s) / self.cur


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
