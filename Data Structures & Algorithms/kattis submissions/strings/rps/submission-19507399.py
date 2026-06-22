import sys

for line in sys.stdin:
    s1 = line.strip()
    s2 = sys.stdin.readline().strip()
    
    if s1 == 'E':
        break
    
    cnt1, cnt2 = 0, 0
    
    for i in range(len(s1)):
        if s1[i] == 'R':
            if s2[i] == 'S':
                cnt1 += 1
            elif s2[i] == 'P':
                cnt2 += 1
        
        elif s1[i] == 'P':
            if s2[i] == 'R':
                cnt1 += 1
            elif s2[i] == 'S':
                cnt2 += 1
            
        else:
            if s2[i] == 'P':
                cnt1 += 1
            elif s2[i] == 'R':
                cnt2 += 1
    
    print("P1: " + str(cnt1))
    print("P2: " + str(cnt2))