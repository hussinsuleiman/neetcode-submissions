n = int(input())

while n != -1:
    total = 0
    curTime = 0
    
    for i in range(n):
        s,t = map(int, input().split())
        total += (t-curTime)*s
        curTime = t
    
    print(str(total) + ' miles')
    n = int(input())