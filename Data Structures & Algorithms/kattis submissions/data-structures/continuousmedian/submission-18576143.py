import sys
import heapq
input = sys.stdin.readline

T = int(input())

for i in range(T):
    N = int(input())
    nbs = list(map(int, input().split()))
    s = 0
    L = []  # max heap (store negatives)
    R = []  # min heap
    
    for x in nbs:
        if not L or x <= -L[0]:
            heapq.heappush(L, -x)
        else:
            heapq.heappush(R, x)
        
        if len(L) > len(R) + 1:
            heapq.heappush(R, -heapq.heappop(L))
        elif len(R) > len(L):
            heapq.heappush(L, -heapq.heappop(R))
        
        if len(R) == len(L):
            s += (-L[0] + R[0]) // 2
        else:
            s += -L[0]
    
    print(s)
    
    