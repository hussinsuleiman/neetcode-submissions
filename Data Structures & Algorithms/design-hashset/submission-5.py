class MyHashSet:
    def __init__(self):
        self.lists = [[] for i in range(2501)]

    def add(self, key: int) -> None:
        if key not in self.lists[key // 400]:
            self.lists[key // 400].append(key)

    def remove(self, key: int) -> None:
        if key in self.lists[key // 400]:
            self.lists[key // 400].remove(key)

    def contains(self, key: int) -> bool:
        return key in self.lists[key // 400]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)