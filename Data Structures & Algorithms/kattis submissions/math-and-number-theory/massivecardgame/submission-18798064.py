import sys
input = sys.stdin.readline

def binSearchLeft(nbCards, i, j, target, N):
    while i <= j:
        mid = (i+j) // 2
        
        if nbCards[mid] >= target:
            j = mid-1
        else:
            i = mid+1

    return j

def binSearchRight(nbCards, i, j, target, N):
    while i <= j:
        mid = (i+j) // 2
        
        if nbCards[mid] <= target:
            i = mid+1
        else:
            j = mid-1
    
    return i

N = int(input())
nbCards = list(map(int, input().split()))
nbCards.sort()
Q = int(input())

for i in range(Q):
    l, r = map(int, input().split())
    left = binSearchLeft(nbCards, 0, N-1, l, N)
    right = binSearchRight(nbCards, 0, N-1, r, N)
    print(right-left-1)