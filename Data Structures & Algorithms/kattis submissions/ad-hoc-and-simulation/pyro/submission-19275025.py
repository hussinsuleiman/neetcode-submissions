import sys
input = sys.stdin.readline

def count_flips(L):
    s = set(L)
    res = []
    
    for x in L:
        cnt = 0
        
        for i in range(32):
            y = x ^ (1<<i)
            
            if y in s and y > x:
                cnt += 1        
        
        for i in range(32):
            for j in range(i+1, 32):
                y = x ^ (1<<i) ^ (1<<j)
                
                if y in s and y > x:
                    cnt += 1
        
        res.append(cnt)
    
    return res
                
L = []
n = int(input())

while n != -1:
    L.append(n)
    n = int(input())
    
res = count_flips(L)

for i in range(len(L)):
    print(str(L[i]) + ':' + str(res[i]))