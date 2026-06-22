t = int(input())

for _ in range(t):
    n,m = map(int, input().split())
    win = True
    
    for i in range(n):
        line = input()
        
        for j in range(m):
            if line[j] == 'W':
                win = not win
    
    if win:
        print('Bob')
    else:
        print('Alice')