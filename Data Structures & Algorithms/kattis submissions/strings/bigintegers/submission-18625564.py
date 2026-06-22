import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    a = input().strip()
    b = input().strip()
    l1 = len(a)
    l2 = len(b)
    lex = 1
    done = False

    for i in range(min(l1, l2)):
        if ord(a[i]) < ord(b[i]):
            lex = 1
            done = True
            break
        elif ord(a[i]) > ord(b[i]):
            done = True
            lex = 2
            break
    
    if not done and l2 < l1:
        lex = 2
    
    bigger = 1
    
    if l1 < l2:
        bigger = 2
    elif l1 > l2:
        bigger = 1
    else:
        for i in range(l1):
            nb1, nb2 = 0, 0
            
            if ord(a[i]) >= ord('0') and ord(a[i]) <= ord('9'):
                nb1 = ord(a[i]) - ord('0')
            
            elif ord(a[i]) >= ord('a') and ord(a[i]) <= ord('z'):
                nb1 = ord(a[i]) - ord('a') + 10
            
            else:
                nb1 = ord(a[i]) - ord('A') + 36
            
            if ord(b[i]) >= ord('0') and ord(b[i]) <= ord('9'):
                nb2 = ord(b[i]) - ord('0')
            
            elif ord(b[i]) >= ord('a') and ord(b[i]) <= ord('z'):
                nb2 = ord(b[i]) - ord('a') + 10
            
            else:
                nb2 = ord(b[i]) - ord('A') + 36
            
            if nb1 < nb2:
                bigger = 2
                break
            elif nb1 > nb2:
                bigger = 1
                break
    
    if (bigger == 2 and lex == 1) or (bigger == 1 and lex == 2):
        sys.stdout.write("YES\n")
    else:
        sys.stdout.write("NO\n")
    