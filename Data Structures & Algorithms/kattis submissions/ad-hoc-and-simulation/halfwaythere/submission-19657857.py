D = input()
l = len(D)
res = ['0']
dec = ('.' in D)
isNeg = (D[0] == '-')

for i in range(l-1, -1, -1):
    if D[i] == '.' or D[i] == '-':
        res.append(D[i])
        continue
    
    d = int(D[i])
    
    if d%2 == 1:
        k = 0
        
        if res[-1] in {'.', '-'}:
            k = int(res[-2]) + 5
            
            if k >= 10:
                res[-2] = str(k-10)
                res.append('1')
                continue
            else:
                res[-2] = str(k)
                
        else:
            k = int(res[-1]) + 5
        
            if k >= 10:
                res[-1] = str(k-10)
                res.append('1')
                continue
            else:
                res[-1] = str(k)
            
            if i == l-1 and not dec:
                res.append('.')
    
    if i == l-1 and res[-1] == '0':
        res[-1] = str(d//2)
    else:
        res.append(str(d//2))

i = len(res)-1

if isNeg:
    i -= 1

while res[i] == '0':
    i -= 1

res = res[:i+1]

if res[-1] == '.':
    res.append('0')
    
    if isNeg:
        res.append('-')
    
elif isNeg:
    res.append('-')

print(''.join(res[::-1]))