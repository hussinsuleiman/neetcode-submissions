import math

n, b = map(int, input().split())
print(int(math.log(n) / math.log(b+1)) + 1)
