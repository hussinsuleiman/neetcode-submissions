import math

res = []
b = 4
cur = 0
i = 2

for k in range(21):
    while cur + math.log(i)/math.log(2) <= b:
        cur += math.log(i)/math.log(2)
        i += 1
    
    res.append(i-1)
    b *= 2

y = int(input())

while y != 0:
    print(res[(y-1960) // 10])
    y = int(input())