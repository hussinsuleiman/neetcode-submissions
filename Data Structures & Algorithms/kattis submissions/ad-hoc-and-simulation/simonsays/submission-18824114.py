N = int(input())

for i in range(N):
    line = input().split()
    
    if len(line) >= 2 and line[0] == 'Simon' and line[1] == 'says':
        line = line[2:]
        print(' ' + ' '.join(line))
    