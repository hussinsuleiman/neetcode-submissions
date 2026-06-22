import math

N = int(input())
divs = [1]

for i in range(2, int(math.sqrt(N)) + 1):
    if N % i == 0:
        divs.append(i)

l = len(divs)

for i in range(l-1, -1, -1):
    if i == l-1 and int(math.sqrt(N)) == math.sqrt(N):
        continue
    
    divs.append(N // divs[i])

for div in divs:
    print(div)