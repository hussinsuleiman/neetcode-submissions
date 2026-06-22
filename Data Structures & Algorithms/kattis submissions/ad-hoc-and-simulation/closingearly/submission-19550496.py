R,S,N = map(int, input().split())
A = list(map(int, input().split()))
cur = 0

if R%S == 0:
    print(0)
    exit()

for i in range(N):
    cur += A[i]
    
    if (cur-R)%S == 0:
        print(i+1)
        exit()

print(-1)