n = input()
res = 0
nbDigits = len(n)

for i in range(nbDigits):
    if n[i] not in {'0', '1', '2'}:
        res += 2 * pow(2, nbDigits-i-1)
        break
    
    if n[i] in {'1', '2'}:
        res += pow(2, nbDigits-i-1)
        
        if n[i] == '1':
            break
    
    if i == nbDigits-1 and n[i] in {'0','2'}:
        res += 1

print(res)