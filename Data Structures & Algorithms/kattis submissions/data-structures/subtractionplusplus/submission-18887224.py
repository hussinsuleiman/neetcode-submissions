N = int(input())
lose = set()
i = 2
nb = 2

while nb <= 5000:
    for j in range(i):
        lose.add(nb+j)
        
    nb += 2*i
    i += 1

if N in lose:
    print("NO")
else:
    print("YES")



