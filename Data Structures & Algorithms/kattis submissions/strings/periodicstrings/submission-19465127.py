s = input()
l = len(s)

for i in range(1, l+1):
    if l%i != 0:
        continue
    
    pattern = s[:i]
    valid = True
    
    for j in range(i, l, i):
        new = s[j:j+i]
        
        for k in range(i):
            if pattern[k] != new[(k+1)%i]:
                valid = False
                break
        
        if not valid:
            break
        
        pattern = new
    
    if valid:
        print(i)
        break