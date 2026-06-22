N = int(input())
names = []

for i in range(N):
    names.append(input().strip())

C = int(input())

for i in range(C):
    event = input().strip().split()
    
    if len(event) == 2:
        for j in range(len(names)):
            if names[j] == event[1]:    
                names = names[:j] + names[j+1:]
                break
    
    else:
        for j in range(len(names)):
            if names[j] == event[1]:    
                names = names[:j] + names[j+1:]
                break
        
        for j in range(len(names)):
            if names[j] == event[2]:
                names = names[:j] + [event[1]] + names[j:]
                break

for name in names:
    print(name)

    