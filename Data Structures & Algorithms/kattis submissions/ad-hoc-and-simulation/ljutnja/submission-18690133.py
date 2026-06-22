import sys
input = sys.stdin.readline

M, N = map(int, input().split())
wishes = []

for i in range(N):
    wishes.append(int(input()))

wishes.sort()
sumAll = sum(wishes) - M
nbBelowAvg = 0
curr = 0
result = 0

while True:
    temp = sumAll // (N - curr)
    
    while nbBelowAvg < N and wishes[nbBelowAvg] <= temp:
        result += wishes[nbBelowAvg] ** 2
        sumAll -= wishes[nbBelowAvg]
        nbBelowAvg += 1
              
    if curr == nbBelowAvg:
        break
        
    curr = nbBelowAvg

q, r = sumAll // (N - curr), sumAll % (N - curr)

for i in range(N - curr - r):
    result += (sumAll // (N - curr)) ** 2

for i in range(r):
    result += (sumAll // (N - curr) + 1) ** 2

print(result)
