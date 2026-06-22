T = int(input())

for _ in range(T):
    input()
    N = int(input())
    names = [input().split() for i in range(N)]
    vals = [int(names[i][1]) for i in range(N)]
    vals.sort()
    tot = 0
    
    for i in range(N):
        tot += abs(vals[i]-i-1)
    
    print(tot)