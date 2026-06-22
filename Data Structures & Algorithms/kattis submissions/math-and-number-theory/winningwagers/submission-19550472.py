N = int(input())
events = input().split()
L = int(input())
tot = 1    

for e in events:
    if e == 'DIE':
        tot *= 6
    elif e == 'COIN':
        tot *= 2
    else:
        tot *= 52

print((tot-1)*L)