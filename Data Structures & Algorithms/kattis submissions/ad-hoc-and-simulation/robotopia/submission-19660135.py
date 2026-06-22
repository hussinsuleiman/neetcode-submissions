n = int(input())

for _ in range(n):
    l1, a1, l2, a2, lt, at = map(int, input().split())
    x,y = at*l1 - lt*a1, a2*l1 - l2*a1
    
    if y == 0:
        if x != 0:
            print('?')
            continue
        
        b = 1
        valid = -1
        done = False
        
        while lt - l2*b > 0:
            if (lt - l2*b)%l1 == 0:
                if valid != -1:
                    print('?')
                    done = True
                    break
                
                valid = b
            
            b += 1
        
        if done:
            continue
        
        if valid == -1:
            print('?')
            continue
        
        a = (lt - l2*valid) // l1
        print(str(a) + ' ' + str(valid))
        continue
    
    if (x*y) <= 0 or abs(x)%abs(y) != 0:
        print('?')
        continue
    
    b = abs(x)//abs(y)
    
    if l1*(lt - l2*b) <= 0 or (lt - l2*b)%l1 != 0:
        print('?')
        continue
    
    a = (lt - l2*b) // l1
    print(str(a) + ' ' + str(b))