i,j = 0, 16**15-1

while i <= j:
    mid = (i+j)//2
    h = []
    temp = mid
    
    while mid != 0:
        if mid%16 > 9:
            h.append(chr(ord('A') + mid%16 - 10))
        else:
            h.append(str(mid%16))
        
        mid //= 16
    
    for k in range(len(h), 15):
        h.append('0')
    
    print('? ' + ''.join(h[::-1]))
    ans = input()
    
    if ans == 'Too high!':
        j = temp-1
    elif ans == 'Too low!':
        i = temp+1
    else:
        exit(0)