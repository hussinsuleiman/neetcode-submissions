t = int(input())

for _ in range(t):
    n,d = map(int, input().split())
    k = 0
    
    while (d+1)**k < n:
        k += 1
    
    print(k)