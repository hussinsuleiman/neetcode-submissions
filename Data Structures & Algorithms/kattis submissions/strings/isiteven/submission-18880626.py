N,K = map(int,input().split())

for i in range(N):
    p = int(input())
    
    while p%2 == 0 and K > 0:
        K -= 1
        p //= 2
    
    if K == 0:
        break

print(1 if K == 0 else 0)