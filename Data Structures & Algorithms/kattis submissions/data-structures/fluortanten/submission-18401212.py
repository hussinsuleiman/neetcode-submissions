import sys
input = sys.stdin.readline

n = int(input())
nbs = list(map(int, input().split()))
nbs.remove(0)
maxSum = 0

for i in range(1, n):
    maxSum += nbs[i-1]*i

currSum = maxSum

for i in range(n-2, -1, -1):
    currSum += nbs[i]
    maxSum = max(maxSum, currSum)

print(maxSum)