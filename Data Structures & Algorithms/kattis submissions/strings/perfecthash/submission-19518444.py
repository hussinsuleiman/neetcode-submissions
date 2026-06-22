n = int(input())
S = [input() for i in range(n)]

for M in range(n, 501):
    good = False
    
    for a in range(M):
        hashes = set()
        valid = True
        
        for s in S:
            h = 0
            
            for i in range(len(s)):
                h = (a * h + ord(s[i])) % M
            
            if h in hashes:
                valid = False
                break
            
            hashes.add(h)
        
        if valid:
            good = True
            break
    
    if good:
        print(str(a) + ' ' + str(M))
        exit()