N = int(input())

for K in range(1, N+1):
    S = int(input())
    vals = input().split()
    blue, red = [], []
    
    for v in vals:
        if v[-1] == 'B':
            blue.append(int(v[:-1]))
        else:
            red.append(int(v[:-1]))
    
    blue.sort()
    red.sort()
    total = 0
    i,j = len(blue)-1, len(red)-1
    
    while i >= 0 and j >= 0:
        total += blue[i] + red[j] - 2
        i -= 1
        j -= 1
    
    print("Case #" + str(K) + ': ' + str(total))