H,N,M = map(int, input().split())
A = (N+1)%2
k = (H-1)*H - (N+A-1)//2 - M

if k >= 0:
    print(A,k)
elif N >= 1:
    print(0,0)
else:
    print(1,0)