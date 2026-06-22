n,k = map(int, input().split())
candies = [int(input()) for i in range(n)]
m = max(candies)
s = sum(candies)

if m*k >= s:
    print(m*k-s)
else:
    print(k*((s+k-1)//k)-s)