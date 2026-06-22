n = int(input())
m = int(input())

if m % 2 == 0 and 2*n <= m and 4*n >= m:
    print((m - 2*n) // 2)
else:
    print("Rong talning")