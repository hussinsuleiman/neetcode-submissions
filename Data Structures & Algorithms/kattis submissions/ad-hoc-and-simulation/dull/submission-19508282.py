N,P,S = map(int, input().split())
dulls = list(map(int, input().split()))
programs = []

for i in range(P):
    size, dull = input().split()
    size = int(size)
    programs.append((size, dull))

execs = list(map(int, input().split()))
zero = input()
cnt = [0]*N
curSize = 0
maxSize = 0

for i in range(S):
    cur = execs[i]
    pSize, pDulls = programs[abs(cur)-1]
    
    if cur > 0:
        curSize += pSize
        
        for p in pDulls:
            if cnt[ord(p)-ord('A')] == 0:
                curSize += dulls[ord(p)-ord('A')] 
                
            cnt[ord(p)-ord('A')] += 1
        
    else:
        curSize -= pSize
        
        for p in pDulls:
            cnt[ord(p)-ord('A')] -= 1
            
            if cnt[ord(p)-ord('A')] == 0:
                curSize -= dulls[ord(p)-ord('A')] 
    
    maxSize = max(maxSize, curSize)

print(maxSize)