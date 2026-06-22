X = float(input())
y = 1000*X*5280/4854

if y-int(y) >= 0.5:
    print(int(y)+1)
else:
    print(int(y))