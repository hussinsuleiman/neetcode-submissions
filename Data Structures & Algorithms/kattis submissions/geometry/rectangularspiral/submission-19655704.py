P = int(input())

for _ in range(P):
    K,x,y = map(int, input().split())
    
    if x < y:
        print(str(K) + ' 2 ' + str(x) + ' ' + str(y))
    elif y >= 4:
        print(str(K) + ' 6 1 2 3 ' + str(5+x-y) + ' ' + str(x+2) + ' ' + str(x+3))
    else:
        print(str(K) + ' NO PATH')