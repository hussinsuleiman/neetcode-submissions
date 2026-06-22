N = int(input())
M = int(input())
times = [int(input()) for i in range(M)]
i,j = 0, max(times)*N

while i <= j:
    mid = (i+j)//2
    nb = 0
    
    for t in range(M):
        nb += mid//times[t]
    
    if nb >= N:
        j = mid-1
    else:
        i = mid+1
    
print(i)