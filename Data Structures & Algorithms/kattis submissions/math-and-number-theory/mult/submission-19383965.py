n = int(input())
i = 0

while i < n:
    start = int(input())
    i += 1
    
    while i < n:
        new = int(input())
        i += 1
        
        if new%start == 0:
            print(new)
            break