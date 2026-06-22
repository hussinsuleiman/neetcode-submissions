import sys
input = sys.stdin.readline

n, s, m = map(int, input().split())
nbs = list(map(int, input().split()))
visit = [False] * n
nbHops = 0

while True:
    if s <= 0:
        print("left")
        break
    
    if s > n:
        print("right")
        break
    
    if visit[s-1]:
        print("cycle")
        break
    
    if nbs[s-1] == m:
        print("magic")
        break
    
    visit[s-1] = True
    s += nbs[s-1]
    nbHops += 1

print(nbHops)