N = int(input())
uni = set()
count = 0

for i in range(N):
    if count == 12:
        break
    
    u,t = input().split()
    
    if u not in uni:
        print(u,t)
        uni.add(u)
        count += 1
    