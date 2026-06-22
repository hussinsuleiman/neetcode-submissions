x1,y1,x2,y2 = map(int, input().split())
res = 2

if x1 in {0, 2024} and y1 in {0, 2024}:
    res -= 1

if x2 in {0, 2024} and y2 in {0, 2024}:
    res -= 1

print(res)