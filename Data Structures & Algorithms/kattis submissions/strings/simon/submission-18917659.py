T = int(input())

for i in range(T):
    s = input().split()
    
    if len(s) >= 2 and s[0] == 'simon' and s[1] == 'says':
        print(' '.join(s[2:]))
    else:
        print()