s = input()
cntT, cntH = 0, 0

for c in s:
    if c == 'T':
        cntT += 1
    else:
        cntH += 1
    
    if max(cntT, cntH) >= 11 and abs(cntT-cntH) >= 2:
        cntT, cntH = 0,0

print(str(cntT) + '-' + str(cntH))