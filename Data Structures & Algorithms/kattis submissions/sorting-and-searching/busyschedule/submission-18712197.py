import sys
input = sys.stdin.readline

n = int(input())

while n != 0:
    times = []
    
    for i in range(n):
        line = input().strip()
        time = line.split()
        hours, minutes = map(int, time[0].split(":"))
        
        m = minutes + (hours % 12) * 60
        order = 0
        
        if time[1] == 'p.m.':
            order = 1
        
        times.append((order, m, line))
    
    times.sort()
    
    for o, m, l in times:
        print(l)
    
    print()
    n = int(input())

    