import sys
input = sys.stdin.readline

print(1)
sys.stdout.flush()
nb = int(input().strip())

while nb < 99:
    if nb%3 == 2:
        print(nb+1)
        sys.stdout.flush()
        if nb == 98:
            break
    else:
        print(nb+2)
        sys.stdout.flush()
        if nb == 97:
            break
    
    nb = int(input().strip())   
