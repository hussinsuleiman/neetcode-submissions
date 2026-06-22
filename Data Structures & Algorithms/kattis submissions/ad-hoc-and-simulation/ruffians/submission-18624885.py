import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    nbs1 = list(map(int, input().strip().split()))
    nbs2 = list(map(int, input().strip().split()))
    done = False
    
    for a in range(5):
        for b in range(5):
            if not done and nbs1[a] == nbs2[b] and a != b:
                print("YES")
                done = True
    
    if not done:
        print("NO")
    