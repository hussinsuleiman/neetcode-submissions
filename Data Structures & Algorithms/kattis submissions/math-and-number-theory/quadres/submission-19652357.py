n = int(input())

for _ in range(n):
    a,p = map(int, input().split())
    a %= p
    
    if a == 0 or p == 2:
        print("yes")
    elif pow(a, (p - 1) // 2, p) == 1:
        print("yes")
    else:
        print("no")