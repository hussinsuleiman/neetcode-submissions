import sys
input = sys.stdin.readline

line = input()

while line != '0\n':
    nbs = list(map(int, line.split()))
    n = nbs[0]
    nbs = nbs[1:]
    
    T = sum(nbs)
    s = T // 2
    dp = [False] * (s+1)
    dp[0] = True
    
    for x in nbs:
        for k in range(s, x - 1, -1):
            if dp[k - x]:
                dp[k] = True

    for k in range(s, -1, -1):
        if dp[k]:
            print(T - k, k)
            break
    
    line = input()

