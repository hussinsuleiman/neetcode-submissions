class MyStack:
    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()

    def push(self, x: int) -> None:
        if not self.queue2:
            self.queue1.append(x)
        else:
            self.queue2.append(x)

    def pop(self) -> int:
        res = 0

        if not self.queue2:
            while self.queue1:
                top = self.queue1.popleft()

                if not self.queue1:
                    res = top
                else:
                    self.queue2.append(top)
        else:
            while self.queue2:
                top = self.queue2.popleft()

                if not self.queue2:
                    res = top
                else:
                    self.queue1.append(top)

        return res

    def top(self) -> int:
        res = 0

        if not self.queue2:
            while self.queue1:
                top = self.queue1.popleft()

                if not self.queue1:
                    res = top
                
                self.queue2.append(top)
        else:
            while self.queue2:
                top = self.queue2.popleft()

                if not self.queue2:
                    res = top
                
                self.queue1.append(top)

        return res

    def empty(self) -> bool:
        return (not self.queue1) and (not self.queue2)


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()