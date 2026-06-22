n = int(input())

for _ in range(n):
    res = list(map(int, input().split()))
    cnt = [0]*4
    
    for k in res:
        cnt[k-1] += 1
    
    index = 0
    
    for i in range(1,4):
        if cnt[i] > cnt[index]:
            index = i
    
    if index == 0:
        print("leader")
    
    elif index == 1:
        print("intellectual")
    
    elif index == 2:
        print("social")
    
    elif index == 3:
        print("practical")