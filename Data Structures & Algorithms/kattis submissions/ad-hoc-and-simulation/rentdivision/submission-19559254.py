N = int(input())
c = [int(input()) for i in range(N)]
R = int(input())
s,m = sum(c), max(c)
pay = (s+R+N-1)//N

if pay < m:
    print("not possible")
    exit()

for k in c:
    print(pay - k)