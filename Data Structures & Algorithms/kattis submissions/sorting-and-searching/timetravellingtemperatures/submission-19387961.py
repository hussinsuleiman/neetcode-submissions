X,Y = map(int, input().split())

if X == 0:
    if Y == 1:
        print("ALL GOOD")
    else:
        print(0)

elif Y == 1:
    print("IMPOSSIBLE")

elif X > 0:
    print(-float(X)/(Y-1))

else:
    print(float(X)/(1-Y))