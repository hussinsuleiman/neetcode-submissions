a,b = map(int, input().split())
c,d = map(int, input().split())
t = int(input())
cost = abs(c-a) + abs(d-b)

if t >= cost and (t-cost)%2 == 0:
    print("Y")
else:
    print("N")