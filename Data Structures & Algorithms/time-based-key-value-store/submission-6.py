class TimeMap:
    def __init__(self):
        self.values = defaultdict(list)
        self.times = defaultdict(list) 

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.values[key].append(value)
        self.times[key].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        i,j = 0, len(self.times[key])-1

        while i <= j:
            mid = (i+j) // 2

            if self.times[key][mid] > timestamp:
                j = mid-1
            else:
                i = mid+1
        
        return self.values[key][j] if j >= 0 else ''  