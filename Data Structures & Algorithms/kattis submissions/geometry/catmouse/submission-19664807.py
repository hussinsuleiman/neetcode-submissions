K = 4.6033388487517004

T = int(input())

for _ in range(T):
    R, t, j = map(int, input().split())
    
    if j < K * t:
        print("YES")
    else:
        print("NO")