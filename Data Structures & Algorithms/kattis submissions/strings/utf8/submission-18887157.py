n = int(input())
types = [0]*4
r = 0

for i in range(n):
    b = input()
    
    if r > 0:
        if b[:2] == '10':
            r -= 1
            continue
        else:
            break
        
    if b[0] == '0':
        types[0] += 1
    elif b[:3] == '110':
        types[1] += 1
        r = 1
    elif b[:4] == '1110':
        types[2] += 1
        r = 2
    elif b[:5] == '11110':
        types[3] += 1
        r = 3
    else:
        r = 1
        break

if r > 0:
    print("invalid")
else:
    for t in types:
        print(t)