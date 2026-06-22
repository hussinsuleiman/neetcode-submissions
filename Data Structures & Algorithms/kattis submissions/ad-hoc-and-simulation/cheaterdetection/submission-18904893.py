N = int(input())

for i in range(N):
    t = float(input())+0.001
    k = int(100*t)
    print("VALID" if k%3 != 2 else "IMPOSSIBLE")