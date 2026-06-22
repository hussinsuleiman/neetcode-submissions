N = int(input())
cnt = {}

for i in range(N):
    n, played, token, target = input().split()
    
    if played in {"Jc", "Jd"}:
        if token == 'R' or (target in cnt and cnt[target] == 2):
            print("INVALID " + n)
            exit()
        
        if target in cnt:    
            cnt[target] += 1
        else:
            cnt[target] = 1
    
    elif played in {"Js", "Jh"}:
        if token == 'P' or (target not in cnt) or (cnt[target] == 0):
            print("INVALID " + n)
            exit()
            
        cnt[target] -= 1
    
    elif played != target or token == 'R':
        print("INVALID " + n)
        exit()
    
    else:
        if target in cnt and cnt[target] == 2:
            print("INVALID " + n)
            exit()
        
        if target in cnt:    
            cnt[target] += 1
        else:
            cnt[target] = 1
    
print("VALID GAME")