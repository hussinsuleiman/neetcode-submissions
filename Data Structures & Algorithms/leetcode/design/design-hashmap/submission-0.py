class MyHashMap:
    def __init__(self):
        self.dico = dict()

    def put(self, key: int, value: int) -> None:
        self.dico[key] = value

    def get(self, key: int) -> int:
        return self.dico[key] if key in self.dico.keys() else -1 

    def remove(self, key: int) -> None:
        if key in self.dico.keys():
            del self.dico[key]


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)