N = int(input())
mini = 101
index = -1

for i in range(N):
    s = input()
    w, l = 0, 0
    tot = 0
    
    for elt in s:
        if elt == 'W':
            w += 1
            if w == 12:
                if mini > tot:
                    mini = tot
                    index = i+1
                break
        else:
            l += 1
            if l == 3:
                w,l = 0,0
                
        tot += 1

if index == -1:
    print("INCOMPLETE")
else:
    print(index)