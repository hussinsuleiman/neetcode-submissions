A,B,C = map(int, input().split())
deps, arrs = [], []
times = []

for _ in range(3):
    arr,dep = map(int, input().split())
    times.append(arr)
    times.append(dep)
    deps.append(dep)
    arrs.append(arr)

times.sort()
deps.sort()
arrs.sort()

i,j = 1,0 
cur = times[0]
nbTrucks = 1
k = 1
res = 0

while k < 6:
    lapse = times[k] - cur
    
    if nbTrucks == 1:
        res += A*lapse
    elif nbTrucks == 2:
        res += B*lapse*2
    elif nbTrucks == 3:
        res += C*lapse*3
    
    while i < 3 and (lapse+cur) == arrs[i]:
        i += 1
        k += 1
        nbTrucks += 1
    
    while j < 3 and (lapse+cur) == deps[j]:
        j += 1
        k += 1
        nbTrucks -= 1
    
    cur += lapse

print(res)