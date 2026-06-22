X = input()
D = len(X)
digits = [X[i] for i in range(D)]
digits.sort()
X = int(X)

for k in range(X+1, 10**D-1):
    s = str(k)
    d = [s[i] for i in range(D)]
    d.sort()
    
    if d == digits:
        print(k)
        exit()

print(0)