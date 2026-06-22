import sys
input = sys.stdin.readline

def count_findable_by_ann(A):
    n = len(A)
    count = 0
    
    for i in range(n):
        low, high = 0, n - 1
        ok = True
        
        while low <= high:
            mid = (low + high) // 2
            if mid == i:
                break   
            if mid < i:
                if A[mid] < A[i]:
                    low = mid + 1
                else:
                    ok = False
                    break
            else: 
                if A[mid] > A[i]:
                    high = mid - 1
                else:
                    ok = False
                    break
        if ok:
            count += 1
    
    return count

n, m, a, c, x0 = map(int, input().split())
seq = []
x = x0

for i in range(n):
    x = (a*x + c) % m 
    seq.append(x)

print(count_findable_by_ann(seq))





