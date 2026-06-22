N = int(input())
nbs = list(map(int, input().split()))
blocks = [(-1)**(nbs[j]) for j in range(N)]
nbOnes, res, i, curSum = sum(nbs), 0, 0, 0

while i < N:
    if blocks[i] + curSum > 0:
        curSum += blocks[i]
        res = max(res, curSum)
    else:
        curSum = 0
        
    i += 1

total = nbOnes + res
print(total if res > 0 else total-1)