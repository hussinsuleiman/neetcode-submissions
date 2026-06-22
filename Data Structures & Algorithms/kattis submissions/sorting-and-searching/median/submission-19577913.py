n = int(input())
nbs = list(map(int, input().split()))
nbs.sort()

if n%2 == 1:
    print(nbs[(n-1)//2])
else:
    print((nbs[(n-1)//2] + nbs[n//2])*0.5)