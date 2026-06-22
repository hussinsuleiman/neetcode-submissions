N = int(input())
res = 0

while N >= (2*res+1)**2:
    N -= (2*res+1)**2
    res += 1
    
print(res)