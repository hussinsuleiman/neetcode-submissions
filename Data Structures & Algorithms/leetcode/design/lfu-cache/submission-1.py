class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_to_freq = {}
        self.freq_to_key = defaultdict(OrderedDict)
        self.minfreq = 0

    def increase_freq(self, key):
        val, freq = self.key_to_freq[key]
        new_freq = freq + 1
        del self.freq_to_key[freq][key]

        if not self.freq_to_key[freq]:
            del self.freq_to_key[freq]

            if freq == self.minfreq:
                self.minfreq += 1
        
        self.key_to_freq[key] = [val, new_freq]
        self.freq_to_key[new_freq][key] = None

    def get(self, key: int) -> int:
        if key not in self.key_to_freq:
            return -1

        self.increase_freq(key)
        return self.key_to_freq[key][0]

    def put(self, key: int, value: int) -> None:
        if key in self.key_to_freq:
            self.key_to_freq[key] = [value, self.key_to_freq[key][1]]
            self.increase_freq(key)
            return
        
        if len(self.key_to_freq) == self.capacity:
            item = self.freq_to_key[self.minfreq].popitem(last=False)
            del self.key_to_freq[item[0]]

            if not self.freq_to_key[self.minfreq]:
                del self.freq_to_key[self.minfreq]

        self.key_to_freq[key] = [value, 1]
        self.freq_to_key[1][key] = None
        self.minfreq = 1


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)