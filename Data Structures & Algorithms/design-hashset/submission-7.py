class MyHashSet:
    def __init__(self):
        self.lists = [[] for i in range(1001)]

    def add(self, key: int) -> None:
        if key not in self.lists[key // 1000]:
            self.lists[key // 1000].append(key)

    def remove(self, key: int) -> None:
        if key in self.lists[key // 1000]:
            self.lists[key // 1000].remove(key)

    def contains(self, key: int) -> bool:
        return key in self.lists[key // 1000]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)