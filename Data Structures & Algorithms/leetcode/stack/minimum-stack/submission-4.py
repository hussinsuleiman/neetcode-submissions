class MinStack:
    stack = []
    stackMin = []

    def __init__(self):
        self.stack = []
        self.stackMin = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if len(self.stackMin) == 0:
            self.stackMin.append(val)
        else:
            self.stackMin.append(min(val, self.stackMin[-1]))


    def pop(self) -> None:
        self.stack.pop()
        self.stackMin.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.stackMin[-1]
        
