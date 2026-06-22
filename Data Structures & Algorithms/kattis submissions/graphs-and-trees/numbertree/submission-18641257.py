import sys
input = sys.stdin.readline

nbs = list(map(str, input().strip().split()))

if len(nbs) == 1:
    print(2**(int(nbs[0])+1)-1)
else:
    H = int(nbs[0])
    s = nbs[1]
    nb = 1

    for i in range(len(s)):
        if s[i] == 'L':
            nb *= 2
        else:
            nb = nb*2 + 1

    print(2**(H+1)-nb)


